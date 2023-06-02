from flask import Blueprint, request
from api.surveys import surveys_service
from api.auth import auth

users_surveys_router = Blueprint('users_surveys_router', __name__)


@users_surveys_router.route('/<id>', methods=['POST'])
@auth
def create(current_user, id):
    return surveys_service.create(current_user, id)