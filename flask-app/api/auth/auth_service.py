from flask import request, jsonify, abort
from models import User
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
import jwt

def sign_in(): 
  auth = request.json

  if not auth or not auth.get('email') or not auth.get('password'):
      return abort(400)

  user = User.query\
      .filter_by(email = auth.get('email'))\
      .first()

  if not user:
      return abort(400)

  if check_password_hash(user.password, auth.get('password')):
      token = jwt.encode({'user_id' : user.user_id, 'exp' : datetime.utcnow() + timedelta(minutes=45)}, "kdxhfds iefhsdbf", "HS256")
      user.date_logged_in = datetime.now()
      db.session.commit()
      return jsonify({"message": "The account has been created.","token": token})

  return abort(400)

def sign_up(): 
  data = request.json
  
  email = data.get('email')
  first_name = data.get('first_name')
  last_name = data.get('last_name')
  phone_number = data.get('phone_number')
  password = data.get('password')

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
          date_logged_in = datetime.now(),
          date_created = datetime.now(),
          password = generate_password_hash(password),
          role = "admin"
      )
      db.session.add(user)
      db.session.commit()

      token = jwt.encode({'user_id' : user.user_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, "kdxhfds iefhsdbf", "HS256")
      return jsonify({"message": "The account has been created.","token": token})
  else:
      return "Ce nom d'utilisateur n'est pas disponible.", 400
