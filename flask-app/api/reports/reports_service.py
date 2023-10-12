from models import Report
from flask import jsonify, send_file
import os

def find_all(current_user):
  reports = Report.query\
        .filter_by(user_id = current_user.user_id)\
        .all()

  return jsonify(reports), 200

def find_one(current_user, id):
  report = Report.query\
        .filter_by(report_id = id, user_id = current_user.user_id)\
        .first()

  return jsonify(report), 200

def find_one_html(current_user, id):
  report = Report.query\
    .filter_by(report_id = id)\
    .first()
  
  if not report:
    return "Not found", 404
  
  if (current_user.user_id != report.user_id and current_user.role != 'admin'):
    return "Unauthorized", 401

  if not os.path.isfile('master_results/{}.pdf'.format(id)):
    return "Not found", 404
  
  return send_file('master_results/{}.html'.format(id), mimetype='text/html')

def find_one_pdf(current_user, id):
  report = Report.query\
    .filter_by(report_id = id)\
    .first()
  
  if not report:
    return "Not found", 404
  
  if (current_user.user_id != report.user_id and current_user.role != 'admin'):
    return "Unauthorized", 401
  
  if not os.path.isfile('master_results/{}.pdf'.format(id)):
    return "Not found", 404
  
  return send_file('master_results/{}.pdf'.format(id), mimetype='application/pdf')




  
