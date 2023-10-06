from flask import Blueprint
from api.reports import reports_service
from api.auth import auth

reports_router = Blueprint('reports_router', __name__)


@reports_router.route('/', methods = ['GET'])
@auth
def find_all(current_user):
  return reports_service.find_all(current_user)


@reports_router.route('/<id>',methods=['GET'])
@auth
def find_one(id, current_user):
  return reports_service.find_one(id, current_user)

