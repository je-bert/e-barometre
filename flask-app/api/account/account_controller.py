from flask import Blueprint
from api.account import account_service
from api.auth import auth

account_router = Blueprint('account_router', __name__)

@account_router.route('/', methods = ['GET'], strict_slashes=False)
@auth
def find_one(current_user):
    return account_service.find_one(current_user)

@account_router.route('/set-password', methods = ['PATCH'], strict_slashes=False)
@auth
def set_password(current_user):
    return account_service.set_password(current_user)

@account_router.route('/update', methods = ['PATCH'], strict_slashes=False)
@auth
def update(current_user):
    return account_service.update(current_user)

@account_router.route('/', methods = ['DELETE'], strict_slashes=False)
@auth
def delete(current_user):
    return account_service.delete(current_user)