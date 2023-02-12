from flask import Blueprint
from admin.auth import auth_service

auth_router = Blueprint('auth_router', __name__)

@auth_router.route('/sign-in', methods =['GET', 'POST'])
def sign_in():
    return auth_service.sign_in()

@auth_router.route('/sign-up', methods =['GET', 'POST'])
def sign_up():
    return auth_service.sign_up()

@auth_router.route('/sign-out')
def sign_out():
    return auth_service.sign_out()