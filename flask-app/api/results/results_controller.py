from flask import Blueprint
from api.results import results_service
from api.auth import auth
import os
from pyhtml2pdf import converter

results_router = Blueprint('results_router', __name__)

@results_router.route('/', methods = ['POST'])
@auth
def generate(current_user):
  return results_service.generate(current_user.user_id)

# Used to fix master template (run only once)
# @results_router.route('/fix', methods = ['GET'])
# def fix():
#   return results_service.convert_xlookup_to_index_match()