from flask import Blueprint
from surveys import surveys_service
from auth import auth

surveys_router = Blueprint('surveys_router', __name__)

@surveys_router.route('/', methods =['GET'])
@auth
def find_all():
    return surveys_service.find_all()

@surveys_router.route('/<id>', methods = ['GET'])
def find_one(id):
  return surveys_service.find_one(id)