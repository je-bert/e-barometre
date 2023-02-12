from flask import Blueprint
from admin.labels import labels_service
from admin.auth import auth

labels_router = Blueprint('labels_router', __name__)

@labels_router.route('/', methods =['GET'])
@auth
def find_all():
    return labels_service.find_all()

@labels_router.route('/update/<id>/<order>', methods = ['GET', 'POST'])
@auth
def update_one(id, order):
  return labels_service.update_one(id, order)

@labels_router.route('/<id>', methods = ['GET'])
@auth
def find_one(id):
  return labels_service.find_one(id)
  
