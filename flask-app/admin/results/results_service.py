from flask import render_template, send_file, abort
from models import User, Report
import os

def find_all():
  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  dir = os.getcwd() + '/master_results/'

  results = []

  for path in os.listdir(dir):
      if os.path.isfile(dir + path):
          report = Report.query\
            .filter_by(report_id = path.split('.')[0])\
            .first()
          if report:
            user = User.query\
              .filter_by(user_id = report.user_id)\
              .first()
            if user:
              results.append({"file": path, "name": user.first_name + " " + user.last_name, "user_id": user.user_id, "report_id": report.report_id})

  return render_template('results.html', results = results)

def export_one(file_name):
  dir = os.getcwd() + '/master_results/'
  if os.path.isfile(dir + file_name):
            return send_file(dir + file_name, as_attachment=True)
  return "Le fichier n'existe pas", 400

def delete_one(file_name):
  dir = os.getcwd() + '/master_results/'
  if os.path.isfile(dir + file_name):
    os.remove(dir + file_name)
    return "Le fichier a été supprimé", 200
  return "Le fichier n'existe pas", 400

def find_one_html(id):
  report = Report.query\
    .filter_by(report_id = id)\
    .first()
  
  if not report:
    return "Not found", 404

  if not os.path.isfile('master_results/{}.html'.format(id)):
    return "Not found", 404
  
  return send_file('master_results/{}.html'.format(id), mimetype='text/html')

def find_one_pdf(id):
  report = Report.query\
    .filter_by(report_id = id)\
    .first()
  
  if not report:
    return "Not found", 404
  
  if not os.path.isfile('master_results/{}.pdf'.format(id)):
    return "Not found", 404
  
  return send_file('master_results/{}.pdf'.format(id), mimetype='application/pdf')


