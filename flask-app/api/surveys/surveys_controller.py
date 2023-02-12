from flask import Blueprint
from api.surveys import surveys_service

surveys_router = Blueprint('surveys_router', __name__)

@surveys_router.route('/')
def find_all():
    return surveys_service.find_all()


@surveys_router.route('/<id>')
def find_one(id):
    return surveys_service.find_one(id)