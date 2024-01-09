from flask import Blueprint
from admin.analysis.sections import sections_service
from admin.auth import auth

sections_router = Blueprint('sections_router',__name__)

@sections_router.route('/<id>',methods=['GET'])
@auth
def find_one(id):
    return sections_service.find_one(id)

@sections_router.route('/',methods=['GET'])
@auth
def find_all():
    return sections_service.find_all()

@sections_router.route('/update/<id>',methods=['GET','POST'])
@auth
def update_one(id):
    return sections_service.update_one(id)

@sections_router.route('/add',methods=['GET','POST'])
@auth
def add_one():
    return sections_service.add_one()

@sections_router.route('/delete/<id>',methods=['GET','POST'])
@auth
def delete_one(id):
    return sections_service.delete_one(id)

