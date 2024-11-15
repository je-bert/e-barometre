from flask import request, jsonify
from models import User
from utils import check_password, check_email
from werkzeug.security import generate_password_hash, check_password_hash
from api.invoices.invoices_service import has_unpaid_invoice, get_user_subscription

from database import db

def find_one(current_user):
  value_to_return = {
    'user_id': current_user.user_id,
    'email': current_user.email,
    'first_name': current_user.first_name,
    'last_name': current_user.last_name,
    'date_created': current_user.date_created,
    'has_unpaid_invoice': has_unpaid_invoice(current_user.user_id),
    'subscription': get_user_subscription(current_user.user_id)
  }
  return jsonify(value_to_return), 200

def set_password(current_user):
    data = request.json
    user_id = current_user.user_id
    current_password = data.get('current_password')
    new_password = data.get('new_password')
    
    if not check_password(new_password):
        return jsonify({"message" : "Nouveau mot de passe ne respecte pas les conditions."}), 400
    
    if not check_password(current_password):
        return jsonify({"message" : "Mot de passe actuel ne respecte pas les conditions."}), 400

    user = User.query\
        .filter_by(user_id = user_id)\
        .first()
    
    if not user:
        return jsonify({"message" : "L'utilisateur a été supprimé."}), 400
    
    if not check_password_hash(user.password, current_password):
        return jsonify({"message" : "Mot de passe actuel invalide."}), 400

    user.password = generate_password_hash(new_password)
    db.session.commit()

    return jsonify({"message" : 'Le mot de passe a été réinitialisé.'}), 200

def update(current_user):
    data = request.json
    user_id = current_user.user_id
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not email or not first_name or not last_name:
        return jsonify({"message" : "Les champs email, first_name et last_name sont obligatoires."}), 400
    
    email = email.lower()
    
    user = User.query\
        .filter_by(user_id = user_id)\
        .first()
    
    if not user:
        return jsonify({"message" : "L'utilisateur a été supprimé."}), 400
    
    if not check_email(email):
        return jsonify({"message" : "Courriel invalide"}), 400
    
    user_with_email = User.query\
        .filter_by(email = email)\
        .first()
    
    if user_with_email and user_with_email.user_id != user_id:
        return jsonify({"message" : "Cette adresse courriel est déjà utilisée"}), 400
    
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    db.session.commit()

    return jsonify({"message" : "L'utilisateur a été mis à jour."}), 200

def delete(current_user):
  user_id = current_user.user_id

  user = User.query\
      .filter_by(user_id = user_id)\
      .first()

  if not user:
      return jsonify({"message" : "L'utilisateur a été supprimé."}), 400

  db.session.delete(user)
  db.session.commit()

  return jsonify({"message" : "L'utilisateur a été supprimé."}), 200
