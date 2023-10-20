from models import Invoice
from flask import jsonify

def find_all(user_id):
  return jsonify(Invoice.query.filter_by(user_id = user_id).all()), 200

def find_one(user_id, invoice_id):
  return jsonify(Invoice.query.filter_by(user_id = user_id, invoice_id = invoice_id).first()), 200

def get_user_subscription(user_id):
  return user_id
  invoice = Invoice.query.filter_by(user_id = user_id, status = "paid").first()
  if not invoice:
    return None
  return invoice.product_id

def has_unpaid_invoice(user_id):
  return Invoice.query.filter_by(user_id = user_id, status = "unpaid").first() != None