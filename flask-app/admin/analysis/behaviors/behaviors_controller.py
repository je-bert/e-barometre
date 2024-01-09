from flask import Blueprint
from admin.analysis.behaviors import behaviors_service
from admin.auth import auth

behaviors_router = Blueprint('behaviors_router',__name__)

@behaviors_router.route('/update/<id>',methods=['GET','POST'])
@auth
def update_one(id):
    return behaviors_service.update_one(id)

@behaviors_router.route('/delete/<id>',methods=['GET','POST'])
@auth
def delete_one(id):
    return behaviors_service.delete_one(id)

@behaviors_router.route('/add/<id>',methods=['GET','POST'])
@auth
def add_one(id):
    return behaviors_service.add_one(id)



