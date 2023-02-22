from flask import Blueprint
from api.auth import auth_service

auth_router = Blueprint('auth_router', __name__)

@auth_router.route('/sign-in', methods =['POST'])
def sign_in():
    return auth_service.sign_in()

@auth_router.route('/sign-up', methods =['POST'])
def sign_up():
    return auth_service.sign_up()

@auth_router.route('/complete-reset-password', methods =['POST'])
def complete_reset_password():
    return auth_service.complete_reset_password()

@auth_router.route('/reset-password', methods =['POST'])
def reset_password():
    return auth_service.reset_password()