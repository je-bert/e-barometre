from models import Invoice
from flask import jsonify

def find_all(user_id):
  return jsonify(Invoice.query.filter_by(user_id = user_id).all()), 200

def find_one(user_id, invoice_id):
  return jsonify(Invoice.query.filter_by(user_id = user_id, invoice_id = invoice_id).first()), 200