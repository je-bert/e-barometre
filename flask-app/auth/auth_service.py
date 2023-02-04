from flask import session, redirect, url_for, render_template, request
from  werkzeug.security import generate_password_hash, check_password_hash
from database import db
from user import User
from datetime import datetime



def sign_in():
    if request.method == 'GET':
        return render_template('sign-in.html'); 
        
    auth = request.form


  
    if not auth or not auth.get('email') or not auth.get('password'):
        return render_template('sign-in.html', error='Invalid credentials.')
  
    user = User.query\
        .filter_by(email = auth.get('email'))\
        .first()


  
    if not user:
        return render_template('sign-in.html', error='Invalid credentials.')
  
    if check_password_hash(user.password, auth.get('password')):
        session['email'] = user.email
        return redirect(url_for('main_router.index'))

    return render_template('sign-in.html', error='Invalid credentials.')
  
def sign_up():
    if request.method == 'GET':
        return render_template('sign-up.html')

    data = request.form
  
    name, email = data.get('name'), data.get('email')
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
        return render_template('sign-up.html', error='User already exists. Please Log in.')


def sign_out():
    session.pop('email', None)
    return redirect(url_for('auth_router.sign_in'))


    