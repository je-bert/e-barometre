from flask import Blueprint, request
from api.users_surveys import users_surveys_service
from api.auth import auth

users_surveys_router = Blueprint('users_surveys_router', __name__)


@users_surveys_router.route('/<id>', methods=['POST'])
@auth
def create(current_user, id):
    return users_surveys.create(current_user, id)