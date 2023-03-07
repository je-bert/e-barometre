from flask import render_template, send_file, abort
from models import User, AnalysisSection
import os
from pycel import ExcelCompiler


def find_all():
  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  dir = os.getcwd() + '/master_results/'

  results = []

  for path in os.listdir(dir):
      if os.path.isfile(dir + path):
          user = User.query\
            .filter_by(user_id = path.split('.')[0])\
            .first()
          if user:
            results.append({"file": path, "name": user.first_name + " " + user.last_name, "user_id": user.user_id})

  return render_template('results.html', results = results)

def find_one(user_id):

  user = User.query\
    .filter_by(user_id = user_id)\
    .first()

  if not user:
    return abort(404)
  
  filename = 'master_results/{}.xlsx'.format(user_id)

  if not os.path.exists(filename):
    return abort(404)
  
  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  sections = AnalysisSection.query\
    .order_by(AnalysisSection.order)\
    .all()
  
  excel = ExcelCompiler(filename=filename)

  sections_to_render = []

  for section in sections:
     sections_to_render.append(render_template('analysis-section.html', section = section, content = generate_content(section.analysis_section_id, excel)))

  return render_template('user-results.html', user = user, sections_to_render = sections_to_render)

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

def generate_content(type, excel):
   #TODO: Validate excel data
  if type == "1":
    cl = excel.evaluate("'TEST_pour PROTOTYPE'!D425") / excel.evaluate("'TEST_pour PROTOTYPE'!G425")
    css = excel.evaluate("'TEST_pour PROTOTYPE'!D426") / excel.evaluate("'TEST_pour PROTOTYPE'!G426")
    ap = excel.evaluate("'TEST_pour PROTOTYPE'!D427") / excel.evaluate("'TEST_pour PROTOTYPE'!G427")
    flag = excel.evaluate("'TEST_pour PROTOTYPE'!I428")
    return render_template('charts/barometer.html', cl = cl, css = css, ap = ap, flag = flag)
  
  elif type == "2":
    series = []
    series.append({
          "name": 'Parent répondant',
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 482)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 482))} for i in range(6)]
    })
    series.append({
          "name": 'Coparent',
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 489)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 489))} for i in range(7)]
    })
    series.append({
          "name": 'Nouveau conjoint·e (lle cas échéant)',
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 497)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 497))} for i in range(5)]
    })
    return render_template('charts/packed-bubbles.html', id = 1, series = series)

  else:
    return render_template('charts/funnel.html')