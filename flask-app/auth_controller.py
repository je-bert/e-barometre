from flask import Blueprint
import auth_service

auth = Blueprint('auth', __name__)

@auth.route('/sign-in', methods =['GET', 'POST'])
def sign_in():
    return auth_service.sign_in()

@auth.route('/sign-up', methods =['GET', 'POST'])
def sign_up():
    return auth_service.sign_up()

@auth.route('/sign-out')
def sign_out():
    return auth_service.sign_out()