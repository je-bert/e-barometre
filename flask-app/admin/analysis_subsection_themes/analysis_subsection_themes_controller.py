from flask import Blueprint
from admin.analysis_subsection_themes import analysis_subsection_themes_service
from admin.auth import auth

analysis_subsection_themes_router = Blueprint('analysis_subsection_themes_router',__name__)

@analysis_subsection_themes_router.route('/<id>',methods=['GET'])
@auth
def find_one(id):
    return analysis_subsection_themes_service.find_one(id)

@analysis_subsection_themes_router.route('/update/<id>',methods=['GET','POST'])
@auth
def update_one(id):
    return analysis_subsection_themes_service.update_one(id)

@analysis_subsection_themes_router.route('/delete/<id>',methods=['GET','POST'])
@auth
def delete_one(id):
    return analysis_subsection_themes_service.delete_one(id)

@analysis_subsection_themes_router.route('/add/<id>',methods=['GET','POST'])
@auth
def add_one(id):
    return analysis_subsection_themes_service.add_one(id)



