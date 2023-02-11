from flask import Blueprint, after_this_request
from db import db_service
from auth import auth



db_router = Blueprint('db_router', __name__)

@db_router.route('/', methods = ['GET'])
@auth
def get():
  return db_service.get()

@db_router.route('/export', methods = ['GET'])
@auth
def export():
  return db_service.export()
  

