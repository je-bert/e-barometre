from flask import Blueprint
from admin.analysis_subsections import analysis_subsections_service
from admin.auth import auth

analysis_subsections_router = Blueprint('analysis_subsections_router',__name__)

@analysis_subsections_router.route('/<id>',methods=['GET'])
@auth
def find_one(id):
    return analysis_subsections_service.find_one(id)

@analysis_subsections_router.route('/',methods=['GET'])
@auth
def find_all():
    return analysis_subsections_service.find_all()

@analysis_subsections_router.route('/update/<id>',methods=['GET','POST'])
@auth
def update_one(id):
    return analysis_subsections_service.update_one(id)

