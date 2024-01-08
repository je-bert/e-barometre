from flask import Blueprint
from admin.analysis_subsection_items import analysis_subsection_items_service
from admin.auth import auth

analysis_subsection_items_router = Blueprint('analysis_subsection_items_router',__name__)

@analysis_subsection_items_router.route('/update/<id>',methods=['GET','POST'])
@auth
def update_one(id):
    return analysis_subsection_items_service.update_one(id)

@analysis_subsection_items_router.route('/add/<id>',methods=['GET','POST'])
@auth
def add_one(id):
    return analysis_subsection_items_service.add_one(id)

@analysis_subsection_items_router.route('/delete/<id>',methods=['GET','POST'])
@auth
def delete_one(id):
    return analysis_subsection_items_service.delete_one(id)

