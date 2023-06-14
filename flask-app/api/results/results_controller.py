from flask import Blueprint
from api.results import results_service
from api.auth import auth

results_router = Blueprint('results_router', __name__)

@results_router.route('/', methods = ['POST'])
def generate():
  return results_service.generate()

@results_router.route('/fix', methods = ['GET'])
def fix():
  return results_service.convert_xlookup_to_index_match()

@results_router.route('/', methods = ['GET'])
def output():
  return results_service.output()

