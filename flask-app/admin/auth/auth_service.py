from flask import session, redirect, url_for, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from models import User
from datetime import datetime

def sign_in():
    if request.method == 'GET':
        if 'email' in session:
            return redirect(url_for('admin_router.auth_router.sign_out'))
        return render_template('sign-in.html'); 
        
    auth = request.form
    next = request.args.get('next')

  
    if not auth or not auth.get('email') or not auth.get('password'):
        return render_template('sign-in.html', error='Identifiants invalides.')
  
    user = User.query\
        .filter_by(email = auth.get('email'))\
        .first()

    if not user:
        return render_template('sign-in.html', error='Identifiants invalides.')
  
    if check_password_hash(user.password, auth.get('password')):
        session['email'] = user.email
        user.date_logged_in = datetime.now()
        db.session.commit()
        return redirect(url_for('main_router.index') if next == None else next)

    return render_template('sign-in.html', error='Identifiants invalides.')
  
def sign_up():
    if request.method == 'GET':
        if 'email' in session:
            return redirect(url_for('admin_router.auth_router.sign_out'))
        return render_template('sign-up.html')

    data = request.form
  
    email = data.get('email')
    password = data.get('password')
  
    # checking for existing user
    user = User.query\
        .filter_by(email = email)\
        .first()

    if not user:
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
    else:
        return render_template('sign-up.html', error="Ce nom d'utilisateur n'est pas disponible.")


def sign_out():
    session.pop('email', None)
    return redirect(url_for('admin_router.auth_router.sign_in'))


    