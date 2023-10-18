from flask import Blueprint, after_this_request
from admin.report_template import report_template_service
from admin.auth import auth

report_template_router = Blueprint('report_template_router', __name__)

@report_template_router.route('/', methods = ['GET'])
@auth
def get_view():
  return report_template_service.get_view()

@report_template_router.route('/import', methods = ['POST'])
@auth
def import_report_template():
  return report_template_service.import_report_template()

@report_template_router.route('/export', methods = ['GET'])
@auth
def export_report_template():
  return report_template_service.export_report_template()
  
@report_template_router.route('/test', methods = ['POST'])
@auth
def test_report_template():
  return report_template_service.test_remport_template()
  

