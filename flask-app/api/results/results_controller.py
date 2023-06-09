from flask import Blueprint
from api.results import results_service
from api.auth import auth

results_router = Blueprint('results_router', __name__)

@results_router.route('/', methods = ['GET'])
@auth
def generate(current_user):
  return results_service.generate(current_user)