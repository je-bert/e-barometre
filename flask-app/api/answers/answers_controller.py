from flask import Blueprint
from api.answers import answers_service
from api.auth import auth

answers_router = Blueprint('answers_router', __name__)


@answers_router.route('/', methods = ['POST'], strict_slashes=False)
@auth
def create(current_user):
    return answers_service.create(current_user)

@answers_router.route('/', methods = ['PUT'], strict_slashes=False)
@auth
def update(current_user):
    return answers_service.update(current_user)