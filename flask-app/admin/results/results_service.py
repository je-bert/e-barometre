from flask import render_template, send_file, abort
from models import User, AnalysisSection, AnalysisSubsection
import os
from database import db
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

  sections = db.session.query(AnalysisSection)\
    .join(AnalysisSubsection)\
    .order_by(AnalysisSection.order)\
    .all()
  
  excel = ExcelCompiler(filename=filename)

  sections_to_render = []

  for section in sections:
    subsections = []
    for subsection in section.subsections:
      subsections.append(render_template('analysis-subsection.html', subsection = subsection, content = generate_content(subsection.schema_type, excel)))
    sections_to_render.append(render_template('analysis-section.html', section = section, subsections = subsections))

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
  if type == "coparenting-dynamics":
    cl = excel.evaluate("'TEST_pour PROTOTYPE'!D425") / excel.evaluate("'TEST_pour PROTOTYPE'!G425")
    css = excel.evaluate("'TEST_pour PROTOTYPE'!D426") / excel.evaluate("'TEST_pour PROTOTYPE'!G426")
    ap = excel.evaluate("'TEST_pour PROTOTYPE'!D427") / excel.evaluate("'TEST_pour PROTOTYPE'!G427")
    flag = excel.evaluate("'TEST_pour PROTOTYPE'!I428")
    return render_template('charts/barometers.html', cl = cl, css = css, ap = ap, flag = flag)
  elif type == "harmful-behaviors-bubbles":
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
    return render_template('charts/packed-bubbles.html', id = type, series = series)
  elif type == "alienating-behaviors-bubbles":
    series = []
    series.append({
          "name": "Nature des comportements aliénants des parents",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(i + 660)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 660))} for i in range(3)]
    })
    series.append({
          "name": "Nature de la réaction de l'enfant",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(i + 667)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 667))} for i in range(3)]
    })
    return render_template('charts/packed-bubbles.html', id = type, series = series) 
  elif type == "child-response-bubbles":
    series = []
    series.append({
          "name": "Alliance",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 579)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 579))} for i in range(2)]
    })
    series.append({
          "name": "Altération/dévoiement de la réalité",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 582)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 582))} for i in range(2)]
    })
    series.append({
          "name": "Chantage affectif, loyauté, manipulation",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 585)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 585))} for i in range(2)]
    })
    series.append({
          "name": "Dénigrement",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 588)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 588))} for i in range(2)]
    })
    series.append({
          "name": "Interférence temps et/ou communication",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 591)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 591))} for i in range(3)]
    })
    series.append({
          "name": "Interférence lien affectif ou symbolique",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 595)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 595))} for i in range(2)]
    })
    series.append({
          "name": "Parentification",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 598)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 598))} for i in range(2)]
    })
    series.append({
          "name": "Rôle actif, Réponse au CC, r",
          "draggable": False,
          "data": [{"name": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 601)), "value": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 601))} for i in range(3)]
    })
    return render_template('charts/packed-bubbles.html', id = type, series = series)
  elif type == "child-behaviors-index":
    value = excel.evaluate("'TEST_pour PROTOTYPE'!C646") / excel.evaluate("'TEST_pour PROTOTYPE'!I646")
    return render_template('charts/barometer.html', id = type, value = value, title = "Sévérité")
  elif type == "funnel":
     data = []
     for i in range(36):
       value = excel.evaluate("'TEST_pour PROTOTYPE'!Y{}".format(i + 608))
       if isinstance(value, int) and value > 0:
          title = excel.evaluate("'TEST_pour PROTOTYPE'!X{}".format(i + 608))
          data.append({"title": title, "value": value})
     data = sorted(data, key=lambda d: d['value'], reverse=True)
     return render_template('charts/funnel_v2.html', elements = data)
  else:
    return type