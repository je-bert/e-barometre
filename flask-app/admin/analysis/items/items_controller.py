from flask import Blueprint
from admin.analysis.items import items_service
from admin.auth import auth

items_router = Blueprint('items_router',__name__)

@items_router.route('/update/<id>',methods=['GET','POST'])
@auth
def update_one(id):
    return items_service.update_one(id)

@items_router.route('/add/<id>',methods=['GET','POST'])
@auth
def add_one(id):
    return items_service.add_one(id)

@items_router.route('/delete/<id>',methods=['GET','POST'])
@auth
def delete_one(id):
    return items_service.delete_one(id)

