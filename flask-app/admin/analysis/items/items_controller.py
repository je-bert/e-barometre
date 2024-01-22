from flask import Blueprint
from admin.analysis.items import items_service
from admin.auth import auth

items_router = Blueprint('items_router',__name__)

@items_router.route('/update/<id>',methods=['GET','POST'])
@auth
def update_one(id):
    return items_service.update_one(id)

@items_router.route('/add/<id>',methods=['POST'])
@auth
def add_one(id):
    return items_service.add_one(id)

@items_router.route('/add-range/<id>/<indicator_id>',methods=['GET'])
@auth
def add_one_range_indicator(id, indicator_id):
    return items_service.add_one(id, 'range', indicator_id)

@items_router.route('/add-range/<id>',methods=['GET'])
@auth
def add_one_range(id):
    return items_service.add_one(id, 'range')

@items_router.route('/add-observation/<id>',methods=['GET'])
@auth
def add_one_observation(id):
    return items_service.add_one(id, 'observation')

@items_router.route('/add-flag-introduction/<id>',methods=['GET'])
@auth
def add_one_flag_introduction(id):
    return items_service.add_one(id, 'flag_introduction')

@items_router.route('/add-red-flag/<id>',methods=['GET'])
@auth
def add_one_red_flag(id):
    return items_service.add_one(id, 'red_flag')

@items_router.route('/add-yellow-flag/<id>',methods=['GET'])
@auth
def add_one_yellow_flag(id):
    return items_service.add_one(id, 'yellow_flag')

@items_router.route('/add-ressource/<id>',methods=['GET'])
@auth
def add_one_ressource(id):
    return items_service.add_one(id, 'ressource')

@items_router.route('/delete/<id>',methods=['GET'])
@auth
def delete_one(id):
    return items_service.delete_one(id)

