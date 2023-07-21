from flask import Blueprint
from api.results import results_service
from api.auth import auth

results_router = Blueprint('results_router', __name__)

@results_router.route('/', methods = ['POST'])
@auth
def generate(current_user):
  return results_service.generate(current_user.user_id)

@results_router.route('/fix', methods = ['GET'])
def fix():
  return results_service.convert_xlookup_to_index_match()

@results_router.route('/', methods = ['GET'])
@auth
def output(current_user):
  return results_service.output(current_user.user_id)


@results_router.route('/demo/<id>',methods=['GET'])
def demo(id):
  return results_service.output(id)

