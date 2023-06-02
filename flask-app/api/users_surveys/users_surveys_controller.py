from flask import Blueprint, request
from api.users_surveys import users_surveys_service
from api.auth import auth

users_surveys_router = Blueprint('users_surveys_router', __name__)

@users_surveys_router.route('/next', methods=['GET'])
@auth
def get_next(current_user):
    return users_surveys_service.get_next(current_user)


@users_surveys_router.route('/', methods=['POST'])
@auth
def create(current_user):
    return users_surveys_service.create(current_user)