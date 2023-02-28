from flask import Blueprint
from admin.analysis_sections import analysis_sections_service
from admin.auth import auth

analysis_sections_router = Blueprint('analysis_sections_router',__name__)


@analysis_sections_router.route('/',methods=['GET'])
@auth
def find_all():
    return analysis_sections_service.find_all()