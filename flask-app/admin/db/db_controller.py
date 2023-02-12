from flask import Blueprint, after_this_request
from admin.db import db_service
from admin.auth import auth

db_router = Blueprint('db_router', __name__)

@db_router.route('/', methods = ['GET'])
@auth
def get_view():
  return db_service.get_view()

@db_router.route('/import', methods = ['POST'])
@auth
def import_db():
  return db_service.import_db()

@db_router.route('/export', methods = ['GET'])
@auth
def export_db():
  return db_service.export_db()

@db_router.route('/reset', methods = ['GET'])
@auth
def reset_db():
  return db_service.reset_db()
  

