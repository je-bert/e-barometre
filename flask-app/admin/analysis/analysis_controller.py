from flask import Blueprint
from admin.analysis.sections import sections_router
from admin.analysis.barometers import barometers_router
from admin.analysis.themes import themes_router
from admin.analysis.items import items_router
from admin.analysis.behaviors import behaviors_router
from admin.analysis.actors import actors_router


analysis_router = Blueprint('analysis_router', __name__)


analysis_router.register_blueprint(sections_router,url_prefix='/sections')
analysis_router.register_blueprint(barometers_router,url_prefix='/barometers')
analysis_router.register_blueprint(themes_router,url_prefix='/themes')
analysis_router.register_blueprint(items_router,url_prefix='/items')
analysis_router.register_blueprint(behaviors_router,url_prefix='/behaviors')
analysis_router.register_blueprint(actors_router,url_prefix='/actors')