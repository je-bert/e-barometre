from flask import Blueprint
from admin.analysis.actors import actors_service 
from admin.auth import auth

actors_router = Blueprint('actors_router',__name__)

@actors_router.route('/update/<id>',methods=['GET','POST'])
@auth
def update_one(id):
    return actors_service.update_one(id)