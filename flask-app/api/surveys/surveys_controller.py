from flask import Blueprint, request
from api.surveys import surveys_service
from api.auth import auth

surveys_router = Blueprint('surveys_router', __name__)

@surveys_router.route('/')
@auth
def find_all(current_user):
    return surveys_service.find_all()


@surveys_router.route('/<id>')
@auth
def find_one(current_user, id):
    return surveys_service.find_one(current_user, id)


@surveys_router.route('/<id>', methods=['PATCH'])
@auth
def update(current_user, id):
    return surveys_service.update(current_user, id)
