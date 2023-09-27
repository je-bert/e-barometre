from flask import jsonify, request
from api.auth import auth
import stripe
import os

stripe_keys = {
    "secret_key": os.environ.get("STRIPE_SECRET_KEY"),
    "publishable_key": os.environ.get("STRIPE_PUBLISHABLE_KEY"),
    "endpoint_secret": os.environ.get("STRIPE_ENDPOINT_SECRET"),
}

stripe.api_key = stripe_keys['secret_key']

def get_publishable_key():
    stripe_config = {"publishable_key": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"  #TODO: change this to the correct url
    stripe.api_key = stripe_keys["secret_key"]

    try:
        checkout_session = stripe.checkout.Session.create(
            #client_reference_id=current_user.id if current_user.is_authenticated else None, # TODO for when buying as authenticated user
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}", #TODO: change this to the correct url
            cancel_url=domain_url + "cancelled", #TODO: change this to the correct url
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "currency": "cad",
                        "product_data": {
                            "name": "Unique",
                        },
                        "unit_amount": 1999,
                    },
                    "quantity": 1,
                }
            ]
        )
        return jsonify({"session_id": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403
    
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, stripe_keys["endpoint_secret"]
        )

    except ValueError as e:
        # Invalid payload
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return "Invalid signature", 400

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        print("Payment was successful.")
        # TODO: run some custom code here

    return "Success", 200