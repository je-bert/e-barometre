from flask import Blueprint
from admin.questions import questions_service
from admin.auth import auth

questions_router = Blueprint('questions_router', __name__)

@questions_router.route('/update/<id>', methods = ['GET', 'POST'])
@auth
def update_one(id):
  return questions_service.update_one(id)
  
@questions_router.route('/add/<id>', methods = ['GET', 'POST'])
@auth
def add_one(id):
  return questions_service.add_one(id)

@questions_router.route('/delete/<id>', methods = ['GET', 'POST'])
@auth
def delete_one(id):
  return questions_service.delete_one(id)

