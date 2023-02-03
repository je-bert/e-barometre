from flask import Blueprint, session
from auth import auth

main_router = Blueprint('main_router', __name__)

@main_router.route('/')
@auth
def index():
    if 'email' in session:
        return f'Logged in as {session["email"]}'
    return "Logged out" 

@main_router.route('/profile')
def profile():
    return 'Profile'