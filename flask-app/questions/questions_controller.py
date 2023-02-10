from flask import Blueprint
from questions import questions_service
from auth import auth

questions_router = Blueprint('questions_router', __name__)

@questions_router.route('/update/<id>', methods = ['GET', 'POST'])
@auth
def update_one(id):
  return questions_service.update_one(id)
  

