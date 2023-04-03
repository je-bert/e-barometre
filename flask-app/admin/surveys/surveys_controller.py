from flask import Blueprint
from admin.surveys import surveys_service
from admin.auth import auth

surveys_router = Blueprint('surveys_router', __name__)

@surveys_router.route('/', methods =['GET'])
@auth
def find_all():
    return surveys_service.find_all()

@surveys_router.route('/update/<id>', methods = ['GET', 'POST'])
@auth
def update_one(id):
  return surveys_service.update_one(id)

@surveys_router.route('/<id>', methods = ['GET'])
@auth
def find_one(id):
  return surveys_service.find_one(id)

@surveys_router.route('/add', methods = ['GET','POST'])
@auth
def add_one(id):
  return surveys_service.add_one(id)
  

