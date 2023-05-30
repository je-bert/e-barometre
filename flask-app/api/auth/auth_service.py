from flask import request, jsonify
from models import User, ResetPasswordToken
import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
import jwt
from mail import send_reset_password, send_confirm_reset_password
from utils import check_password, check_email
from uuid import uuid4

def sign_in(): 
  auth = request.json

  password = auth.get('password')
  email = auth.get('email')

  print(password)

  if not auth or not email or not password:
      return 'Identifiants invalides.', 400
    
  if not check_password(password) or not check_email(email):
    return 'Identifiants invalides.', 400

  user = User.query\
      .filter_by(email = auth.get('email'))\
      .first()

  if not user:
      return 'Identifiants invalides.', 400

  if check_password_hash(user.password, auth.get('password')):
      token = jwt.encode({'user_id' : user.user_id, 'exp' : datetime.utcnow() + timedelta(minutes=45)}, "kdxhfds iefhsdbf", "HS256")
      user.date_logged_in = datetime.datetime.now()
      db.session.commit()
      return jsonify({"message": "The account has been created.","token": token})

  return 'Identifiants invalides.', 400

def sign_up(): 
  data = request.json
  
  email = data.get('email')
  first_name = data.get('first_name')
  last_name = data.get('last_name')
  phone_number = data.get('phone_number')
  password = data.get('password')

  if not check_email(email):
        return 'Courriel invalide.', 400

  if not check_password(password):
      return 'Mot de passe invalide.', 400

  # checking for existing user
  user = User.query\
      .filter_by(email = email)\
      .first()

  if not user:
      user = User(
          first_name = first_name,
          last_name = last_name,
          email = email,
          phone_number = phone_number, 
          date_logged_in = datetime.datetime.now(),
          date_created = datetime.datetime.now(),
          password = generate_password_hash(password),
          role = "admin"
      )
      db.session.add(user)
      db.session.commit()

      token = jwt.encode({'user_id' : user.user_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, "kdxhfds iefhsdbf", "HS256")
      return jsonify({"message": "The account has been created.","token": token})
  else:
      return "Ce nom d'utilisateur n'est pas disponible.", 400


def complete_reset_password():
    data = request.json
    user_id = data.get('id')
    token = data.get('token')
    password = data.get('password')

    if not user_id or not token:
        return "Le lien est invalide.", 400
    
    if not check_password(password):
        return "Mot de passe invalide", 400
    
    reset_password_token = ResetPasswordToken.query\
        .filter_by(user_id = user_id)\
        .first()

    if not reset_password_token or not check_password_hash(reset_password_token.token, token): 
        return "Le lien est invalide.", 400

    db.session.delete(reset_password_token)
    db.session.commit()

    delta = datetime.datetime.now() - reset_password_token.date_created
    if delta.total_seconds() > 600:
        return "Le lien est expiré.", 400

    user = User.query\
        .filter_by(user_id = user_id)\
        .first()

    if not user:
        return "L'utilisateur a été supprimé.", 400

    user.password = generate_password_hash(password)
    db.session.commit()

    send_confirm_reset_password(user.email)

    return "Le courriel a été réinitialisé.", 200

def reset_password():
    email = request.json.get('email')

    if not email or not check_email(email):
        return "Courriel invalide", 400

    user = User.query\
        .filter_by(email = email)\
        .first()

    if not user:
        return "Cet utilisateur n'existe pas", 400

    token_str = str(uuid4())
    
    send_reset_password(user.email, user.user_id, token_str)

    token = ResetPasswordToken(
        user_id = user.user_id,
        token = generate_password_hash(token_str),
        date_created = datetime.datetime.now(),
    )
    db.session.merge(token)
    db.session.commit()

    return "Un courriel a été envoyé.", 200
    
