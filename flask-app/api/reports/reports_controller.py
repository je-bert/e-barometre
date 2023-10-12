from flask import Blueprint
from api.reports import reports_service
from questions import questions_service
from api.auth import auth

reports_router = Blueprint('reports_router', __name__)

## TODO : Remove this route
@reports_router.route('/test', methods = ['GET'])
def find_questions():
  return questions_service.generate_gradients(0)

@reports_router.route('/', methods = ['GET'])
@auth
def find_all(current_user):
  return reports_service.find_all(current_user)

@reports_router.route('/<id>/pdf',methods=['GET'])
@auth
def find_one_pdf(current_user, id):
  return reports_service.find_one_pdf(current_user, id)

@reports_router.route('/<id>/html',methods=['GET'])
@auth
def find_one_html(current_user, id):
  return reports_service.find_one_html(current_user, id)

@reports_router.route('/<id>',methods=['GET'])
@auth
def find_one( current_user, id):
  return reports_service.find_one(current_user, id)
