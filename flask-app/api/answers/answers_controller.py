from flask import Blueprint
from api.answers import answers_service

answers_router = Blueprint('answers_router', __name__)

@answers_router.route('/', methods = ['PUT'], strict_slashes=False)
def update():
    return answers_service.update()