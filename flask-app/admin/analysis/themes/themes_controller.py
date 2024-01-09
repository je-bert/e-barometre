from flask import Blueprint
from admin.analysis.themes import themes_service
from admin.auth import auth

themes_router = Blueprint('themes_router',__name__)

@themes_router.route('/<id>',methods=['GET'])
@auth
def find_one(id):
    return themes_service.find_one(id)

@themes_router.route('/update/<id>',methods=['GET','POST'])
@auth
def update_one(id):
    return themes_service.update_one(id)

@themes_router.route('/delete/<id>',methods=['GET','POST'])
@auth
def delete_one(id):
    return themes_service.delete_one(id)

@themes_router.route('/add/<id>',methods=['GET','POST'])
@auth
def add_one(id):
    return themes_service.add_one(id)



