from flask import Blueprint
from api.reports import reports_service
from api.auth import auth

reports_router = Blueprint('reports_router', __name__)


@reports_router.route('/', methods = ['GET'])
@auth
def findAll(current_user):
  return reports_service.findAll(current_user)


@reports_router.route('/<id>',methods=['GET'])
@auth
def findOne(id, current_user):
  return reports_service.findOne(id, current_user)

