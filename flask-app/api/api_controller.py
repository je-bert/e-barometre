from flask import Blueprint
from .surveys import surveys_router
from .answers import answers_router

api_router = Blueprint('api_router', __name__)

api_router.register_blueprint(surveys_router, url_prefix='/surveys')
api_router.register_blueprint(answers_router, url_prefix='/answers')