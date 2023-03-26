from flask import Blueprint
from admin.label_items import label_items_service
from admin.auth import auth

label_items_router = Blueprint('label_items_router', __name__)

@label_items_router.route('/update/<id>', methods = ['GET', 'POST'])
@auth
def update_one(id):
  return label_items_service.update_one(id)
  

