from flask import jsonify, request
from api.auth import auth
import stripe
import os
from database import db
from models import User, Invoice
from werkzeug.security import generate_password_hash
from datetime import datetime
from mail import send_account_created, send_payment_failed
from dateutil.relativedelta import relativedelta
from utils import check_email
import random
import string
from crontab import crontab

stripe_keys = {
  "secret_key": os.environ.get("STRIPE_SECRET_KEY"),
  "publishable_key": os.environ.get("STRIPE_PUBLISHABLE_KEY"),
  "endpoint_secret": os.environ.get("STRIPE_ENDPOINT_SECRET"),
}

products = {
  "temporary": os.environ.get("STRIPE_TEMPORARY_PRODUCT_ID"),
  "unique": os.environ.get("STRIPE_UNIQUE_PRODUCT_ID"),
  "multiple": os.environ.get("STRIPE_MULTIPLE_PRODUCT_ID"),
}

expirations = {
  os.environ.get("STRIPE_TEMPORARY_PRODUCT_ID"): relativedelta(days=7),
  os.environ.get("STRIPE_UNIQUE_PRODUCT_ID"): relativedelta(months=3),
  os.environ.get("STRIPE_MULTIPLE_PRODUCT_ID"): relativedelta(years=1)
}

domain_url = "https://e-demo2.netlify.app/"  #TODO: change this to the correct url
success_url = domain_url + "ebarometre?status=success&session_id={CHECKOUT_SESSION_ID}"
cancel_url = domain_url + "ebarometre?status=cancelled"

def generate_password():
  # Define character sets
  lowercase_letters = string.ascii_lowercase
  uppercase_letters = string.ascii_uppercase
  digits = string.digits
  special_symbols = "!@#$%&*+?"

  # Ensure at least one character from each set
  password = (
      random.choice(lowercase_letters) +
      random.choice(uppercase_letters) +
      random.choice(digits) +
      random.choice(special_symbols)
  )

  # Fill the rest of the password with random characters
  password_length = 10  # Total password length
  remaining_length = password_length - 4  # 4 characters already chosen
  all_characters = lowercase_letters + uppercase_letters + digits + special_symbols

  for _ in range(remaining_length):
      password += random.choice(all_characters)

  # Shuffle the characters to make it random
  password_list = list(password)
  random.shuffle(password_list)
  return ''.join(password_list)

def get_user(session):
    email = session["customer_details"]["email"].lower()

    # checking for existing user
    user = User.query\
        .filter_by(email = email)\
        .first()
    
    if user:
        return user, None
    
    password = generate_password()

    name = session["customer_details"]["name"]
    # Split the name into words
    name_parts = name.split() if name != None else []
    # The first name is all words except the last one
    first_name = " ".join(name_parts[:-1]) if len(name_parts) > 1 else ""
    # The last name is the last word    
    last_name = name_parts[-1] if len(name_parts) > 0 else ""
    user = User(
        first_name = first_name,
        last_name = last_name,
        email = email,
        date_logged_in = datetime.now(),
        date_created = datetime.now(),
        password = generate_password_hash(password),
        role = "user"
    )
    db.session.add(user)

    return user, password

def create_invoice(user, session, status = 'paid'):
    product = session['line_items']["data"][0]
    
    if product == None:
      #error
      return "Invalid product", 400

    #find existing invoice
    invoice = Invoice.query\
        .filter_by(session_id = session["id"])\
        .first()
    
    if not invoice:
        # Create invoice
        invoice = Invoice(
            user_id = user.user_id,
            amount_subtotal = product["amount_subtotal"],
            amount_tax = product["amount_tax"],
            amount_discount = product["amount_discount"],
            amount_total = product["amount_total"],
            price_id = product["price"]["id"],
            status = status,
            date_expiration = datetime.now() + expirations[product["price"]["id"]],
            date_created = datetime.now(),
            session_id = session["id"],
            description = product["description"]
        )
        db.session.add(invoice)
    else:
        invoice.status = status
        invoice.date_expiration = datetime.now() + expirations[product["price"]["id"]]
    
    

def fulfill_order(session, status = 'paid'):
  print("Fulfilling order")
  user, password = get_user(session)
  if password:
     send_account_created(user.email, password)
  create_invoice(user, session, status)
  db.session.commit()


stripe.api_key = stripe_keys['secret_key']

def get_publishable_key():
    stripe_config = {"publishable_key": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

def create_checkout_session():
    data = request.get_json()
    if not data or not "productId" in data or not "email" in data:
        return "Invalid body", 400
    
    product_id = data["productId"]
    email = data["email"].lower()

    if not check_email(email):
        return "Invalid email", 400

    if product_id not in products:
        return "Invalid product id", 400
    
    user = User.query\
        .filter_by(email = email)\
        .first()
    
    if user:
        existingInvoice = Invoice.query\
        .filter_by(user_id = user.user_id, status = "paid", price_id = products[product_id])\
        .first()

        if existingInvoice and existingInvoice.date_expiration > datetime.now():
            return "User already has this product", 400

    stripe.api_key = stripe_keys["secret_key"]

    try:
        checkout_session = stripe.checkout.Session.create(
            customer_email=email,
            success_url=success_url,
            cancel_url=cancel_url,
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price": products[product_id],
                    "quantity": 1,
                }
            ]
        )
        return jsonify({"session_id": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 400
    
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, stripe_keys["endpoint_secret"]
        )

    except ValueError as e:
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        return "Invalid signature", 400

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session = stripe.checkout.Session.retrieve(session["id"], expand=["line_items"])
        fulfill_order(session, 'pending')
        if session.payment_status == "paid":
          fulfill_order(session, 'paid')

    elif event['type'] == 'checkout.session.async_payment_succeeded':
        session = event['data']['object']
        session = stripe.checkout.Session.retrieve(session["id"], expand=["line_items"])
        fulfill_order(session, 'paid')

    elif event['type'] == 'checkout.session.async_payment_failed':
        session = event['data']['object']
        session = stripe.checkout.Session.retrieve(session["id"], expand=["line_items"])
        fulfill_order(session, 'failed')
        # Send an email to the customer asking them to retry their order
        print("Emailing customer for failed payment")
        send_payment_failed(session["customer_details"]["email"])
       
    return "Success", 200

@crontab.job()
def update_expired_invoices():
    print("Updating expired invoices")
    invoices = Invoice.query\
      .filter(Invoice.status == "paid", Invoice.date_expiration < datetime.now())\
      .all()
    
    for invoice in invoices:
      invoice.status = "expired"
      if (invoice.price_id == os.environ.get("STRIPE_MULTIPLE_PRODUCT_ID")):
        user = User.query\
          .filter_by(user_id = invoice.user_id)\
          .first()
        if user:
          try:
            checkout_session = stripe.checkout.Session.create(
                customer_email=user.email,
                success_url=success_url,
                cancel_url=cancel_url,
                payment_method_types=["card"],
                mode="payment",
                line_items=[
                    {
                        "price": products["multiple"],
                        "quantity": 1,
                    }
                ]
            )
            session = stripe.checkout.Session.retrieve(checkout_session["id"], expand=["line_items"])
            product = session['line_items']["data"][0]
            if product:
              newInvoice = Invoice(
                user_id = user.user_id,
                amount_subtotal = product["amount_subtotal"],
                amount_tax = product["amount_tax"],
                amount_discount = product["amount_discount"],
                amount_total = product["amount_total"],
                price_id = product["price"]["id"],
                status = 'unpaid',
                date_expiration = datetime.now() + expirations[product["price"]["id"]],
                date_created = datetime.now(),
                session_id = session["id"],
                description = product["description"]
            )
            db.session.add(newInvoice)
            #TODO: Send email with link to app to pay the invoice
          except Exception as e:
            print(e)
          
      db.session.commit()
      continue