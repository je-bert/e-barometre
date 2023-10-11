from flask import Blueprint
from api.results import results_service
from api.auth import auth
import pdfkit

results_router = Blueprint('results_router', __name__)

@results_router.route('/', methods = ['POST'])
@auth
def generate(current_user):
  return results_service.generate(current_user.user_id)

# @results_router.route('/fix', methods = ['GET'])
# def fix():
#   return results_service.convert_xlookup_to_index_match()

@results_router.route('/', methods = ['GET'])
@auth
def output(current_user):
  html = results_service.output(current_user.user_id)
  options = {
      'page-size': 'Letter',
      'margin-top': '0in',
      'margin-right': '0in',
      'margin-bottom': '0in',
      'margin-left': '0in',
      'encoding': "UTF-8",
      'custom-header': [
          ('Accept-Encoding', 'gzip')
      ],
      'no-outline': None
  }
  print(html)
  pdfkit.from_string(html, "test.pdf", options=options)
  return



@results_router.route('/<id>',methods=['GET'])
def demo(id):
  return results_service.output(id)

