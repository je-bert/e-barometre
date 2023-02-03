from flask import Blueprint, session
from auth_decorator import auth

main = Blueprint('main', __name__)

@main.route('/')
@auth
def index():
    if 'email' in session:
        return f'Logged in as {session["email"]}'
    return "Logged out" 

@main.route('/profile')
def profile():
    return 'Profile'