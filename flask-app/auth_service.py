from flask import session, redirect, url_for, render_template, request
from  werkzeug.security import generate_password_hash, check_password_hash
import uuid
from database import db
from user_model import User

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
        return redirect(url_for('main.index'))

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
            public_id = str(uuid.uuid4()),
            name = name,
            email = email,
            password = generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        session['email'] = request.form['email']
        return redirect(url_for('main.index'))
    else:
        return render_template('sign-up.html', error='User already exists. Please Log in.')


def sign_out():
    session.pop('email', None)
    return redirect(url_for('auth.sign_in'))


    