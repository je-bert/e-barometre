from flask import Blueprint
from admin.results import results_service
from admin.auth import auth

results_router = Blueprint('results_router', __name__)

@results_router.route('/', methods = ['GET'])
@auth
def find_all():
  return results_service.find_all()

@results_router.route('/<user_id>', methods = ['GET'])
@auth
def find_one(user_id):
  return results_service.find_one(user_id)

@results_router.route('/export/<file_name>', methods = ['GET'])
@auth
def export_one(file_name):
  return results_service.export_one(file_name)

@results_router.route('/delete/<file_name>', methods = ['GET'])
@auth
def delete_one(file_name):
  return results_service.delete_one(file_name)

  
