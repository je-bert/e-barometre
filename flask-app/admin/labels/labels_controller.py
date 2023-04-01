from flask import Blueprint
from admin.labels import labels_service
from admin.auth import auth

labels_router = Blueprint('labels_router', __name__)

@labels_router.route('/', methods =['GET'])
@auth
def find_all():
    return labels_service.find_all()

@labels_router.route('/update/<id>', methods = ['GET', 'POST'])
@auth
def update_one(id):
  return labels_service.update_one(id)

@labels_router.route('/<id>', methods = ['GET'])
@auth
def find_one(id):
  return labels_service.find_one(id)

@labels_router.route('/add', methods = ['GET','POST'])
@auth
def add_one():
  return labels_service.add_one()
  
