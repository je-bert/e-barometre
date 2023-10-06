from flask import Blueprint
from .surveys import surveys_router
from .answers import answers_router
from .auth import auth_router
from .users_surveys import users_surveys_router
from .results import results_router
from .account import account_router
from .stripe import stripe_router
from .invoices import invoices_router
from .reports import reports_router

api_router = Blueprint('api_router', __name__)

api_router.register_blueprint(surveys_router, url_prefix='/surveys')
api_router.register_blueprint(users_surveys_router, url_prefix='/users_surveys')
api_router.register_blueprint(answers_router, url_prefix='/answers')
api_router.register_blueprint(auth_router, url_prefix='/auth')
api_router.register_blueprint(results_router, url_prefix='/results')
api_router.register_blueprint(account_router, url_prefix='/account')
api_router.register_blueprint(stripe_router, url_prefix='/stripe')
api_router.register_blueprint(invoices_router, url_prefix='/invoices')
api_router.register_blueprint(reports_router, url_prefix='/reports')