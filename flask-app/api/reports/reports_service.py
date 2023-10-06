from models import Report
from flask import jsonify

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
