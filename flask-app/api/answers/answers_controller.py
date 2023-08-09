from flask import Blueprint
from api.answers import answers_service
from api.auth import auth

answers_router = Blueprint('answers_router', __name__)

@answers_router.route('/', methods = ['POST','PUT', 'DELETE'], strict_slashes=False)
@auth
def update(current_user):
    return answers_service.update(current_user)

@answers_router.route('/<question_id>', methods = ['GET'], strict_slashes=False)
@auth
def find_one(current_user, question_id):
    return answers_service.find_one(current_user, question_id)

@answers_router.route('/', methods = ['GET'], strict_slashes=False)
@auth
def find_all(current_user):
    return answers_service.find_all(current_user)