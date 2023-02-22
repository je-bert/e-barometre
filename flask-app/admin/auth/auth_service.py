from flask import session, redirect, url_for, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from models import User, ResetPasswordToken
from datetime import datetime
from utils import check_email, check_password
from uuid import uuid4

def sign_in():
    if request.method == 'GET':
        if 'email' in session:
            return redirect(url_for('admin_router.auth_router.sign_out'))
        return render_template('sign-in.html'); 
        
    auth = request.form
    if not auth:
        return 'Identifiants invalides.', 400

    email = auth.get('email')
    password = auth.get('password')
    #If the inputs is not respecting formats, don't look for user
    if not check_password(password) or not check_email(email):
        return 'Identifiants invalides.', 400
  
    user = User.query\
        .filter_by(email = email)\
        .first()

    if not user:
        return 'Identifiants invalides.', 400
    
    if user.role != 'admin':
        return "Vous n'avez pas les autorisations requises.", 403

    if check_password_hash(user.password, password):
        next = request.args.get('next')
        session['email'] = user.email
        user.date_logged_in = datetime.now()
        db.session.commit()
        return redirect(url_for('main_router.index') if next == None else next)
    return 'Identifiants invalides.', 400
  
def sign_up():
    if request.method == 'GET':
        if 'email' in session:
            return redirect(url_for('admin_router.auth_router.sign_out'))
        return render_template('sign-up.html')

    #TODO: Comment seront cree les comptes admin?
    auth = request.form
  
    if not auth:
        return 'Formulaire invalide.', 400

    email = auth.get('email')
    password = auth.get('password')

    if not check_email(email):
        return 'Courriel invalide.', 400

    if not check_password(password):
        return 'Mot de passe invalide.', 400
  
    # checking for existing user
    user = User.query\
        .filter_by(email = email)\
        .first()

    if user != None:
       "Ce nom d'utilisateur n'est pas disponible.", 400

    user = User(
        first_name = "test",
        last_name = "test",
        email = email,
        phone_number = "418-888-8888",
        date_logged_in = datetime.now(),
        date_created = datetime.now(),
        password = generate_password_hash(password),
        role = "admin"
    )
    db.session.add(user)
    db.session.commit()

    session['email'] = request.form['email']
    return redirect(url_for('main_router.index'))


def sign_out():
    session.pop('email', None)
    return redirect(url_for('admin_router.auth_router.sign_in'))

def complete_reset_password():
    if request.method == 'GET':
        if 'email' in session:
            return redirect(url_for('admin_router.auth_router.sign_out'))
        user_id = request.args.get('id')
        token = request.args.get('token')
        return render_template('complete-reset-password.html', user_id = user_id, token = token) 

    user_id = request.form.get('user_id')
    token = request.form.get('token')
    password = request.form.get('password')

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

    delta = datetime.now() - reset_password_token.date_created
    if delta.total_seconds() > 600:
        return "Le lien est expiré.", 400

    user = User.query\
        .filter_by(user_id = user_id)\
        .first()

    if not user:
        return "L'utilisateur a été supprimé.", 400

    user.password = generate_password_hash(password)
    db.session.commit()

    #TODO: Send confirm reset password email to the user

    return redirect(url_for('admin_router.auth_router.sign_in'))

def reset_password():
    if request.method == 'GET':
        if 'email' in session:
            return redirect(url_for('admin_router.auth_router.sign_out'))
        return render_template('reset-password.html')

    email = request.form.get('email')

    if not email:
        return "Courriel invalide", 400

    user = User.query\
        .filter_by(email = email)\
        .first()

    if not user:
        return "Cet utilisateur n'existe pas", 400

    token_str = str(uuid4())

    #TODO: Send email with reset link to user

    token = ResetPasswordToken(
        user_id = user.user_id,
        token = generate_password_hash(token_str),
        date_created = datetime.now(),
    )
    db.session.merge(token)
    db.session.commit()

    return "Un courriel a été envoyé.", 200
    
    



    