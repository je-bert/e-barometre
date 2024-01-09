from flask import Blueprint
from admin.analysis.barometers import barometers_service
from admin.auth import auth

barometers_router = Blueprint('barometers_router',__name__)

@barometers_router.route('/<id>',methods=['GET'])
@auth
def find_one(id):
    return barometers_service.find_one(id)

@barometers_router.route('/update/<id>',methods=['GET','POST'])
@auth
def update_one(id):
    return barometers_service.update_one(id)

@barometers_router.route('/delete/<id>',methods=['GET','POST'])
@auth
def delete_one(id):
    return barometers_service.delete_one(id)

@barometers_router.route('/add/<id>',methods=['GET','POST'])
@auth
def add_one(id):
    return barometers_service.add_one(id)



