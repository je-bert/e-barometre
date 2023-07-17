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
      return abort(400)

  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  filename = 'master_results/{}.xlsx'.format(user_id)

  if not os.path.exists(filename):
     return abort(404)
  
  worksheet_name = 'Test de contenu du rapport'

  sections = db.session.query(AnalysisSection)\
    .join(AnalysisSubsection)\
    .order_by(AnalysisSection.order)\
    .all()
  
  excel = ExcelCompiler(filename=filename)

  sections = []
  themes = []
  flag_introduction = None
  yellow_flags = []
  red_flags = []
  previous_cell = None
  about = None

  for i in range (1, 400):
    cell = excel.evaluate(f"'{worksheet_name}'!D{i}")
    if cell and cell != '' and cell != ' ':
      value = excel.evaluate(f"'{worksheet_name}'!E{i}")
      if previous_cell == 'red_flag' and cell != 'red_flag':
        sections.append(render_template('reports/themes.html', analysis_items = themes, observations = themes))
        if len(red_flags) > 0 or len(yellow_flags) > 0:
          sections.append(render_template('reports/flags.html', yellow_flags = yellow_flags, red_flags = red_flags, flag_introduction = flag_introduction))
        themes = []
        yellow_flags = []
        red_flags = []
        flag_introduction = None
        about = None
      elif not value or value == '' or value == ' ' or value == 0:
        continue
      elif cell == 'section-title':
        sections.append(render_template('reports/section-title.html', content = value))
      elif cell == 'subsection-title':
        sections.append(render_template('reports/subsection-title.html', content = value))
      elif cell == 'about-barometer':
        sections.append(render_template('reports/about-barometer.html', content = value))
        about = value
      elif cell == 'barometer':
        if value == 'barometer-1' or value == 'barometer-5':
          sections.pop()
          sections.append(render_template('reports/about-barometer.html', content = about, hide_lg = True))
        sections.append(render_template("reports/report-1/" + value + ".html", data = generate_barometer_data(value, excel, about), about = about))
      elif cell == 'ressources':
        sections.append(render_template('reports/ressources.html', content = value))
      elif cell == 'theme':
        themes.append(value)
      elif cell == 'flag_introduction':
        flag_introduction = value
      elif cell == 'yellow_flag':
        yellow_flags.append(value)
      elif cell == 'red_flag':
        red_flags.append(value)
      previous_cell = cell

  return render_template('reports/report-1/base.html', children = sections)

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

def generate_barometer_data(barometer, excel, about):
  if barometer == "barometer-1":
    data = {
      "id": "barometer_1",
      "value": excel.evaluate("'TEST_pour PROTOTYPE'!C438"),
      "range": [
        {
          "name": excel.evaluate("'TEST_pour PROTOTYPE'!G{}".format(i + 438)),
          "min": excel.evaluate("'TEST_pour PROTOTYPE'!H{}".format(i + 438)),
          "max": excel.evaluate("'TEST_pour PROTOTYPE'!I{}".format(i + 438)),
        } for i in range(4)
      ] ,
    }
    for r in data['range']:
      if r['min'] <= data['value'] <= r['max']:
        data['result'] = r['name']
        break
    data['value'] = (data['value'] / data['range'][3]['max']) * 100
    data['green'] = (data['range'][0]['max'] / data['range'][3]['max']) * 100
    data['yellow'] = (data['range'][1]['max'] / data['range'][3]['max']) * 100
    data['orange'] = (data['range'][2]['max'] / data['range'][3]['max']) * 100
    return data
  elif barometer == "barometer-2":
    data = {
      "id": "barometer_2",
      "label_1": excel.evaluate("'TEST_pour PROTOTYPE'!E453"),
      "label_2": excel.evaluate("'TEST_pour PROTOTYPE'!D453"),
      "items":[
        {
          "name": excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(i + 455)),
          "value_1": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 455)),
          "value_2": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 455))
        } for i in range(8) if excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(i + 455))
      ],
    }
    # Sort the items based on the difference between first_value and second_value
    data['items'] = sorted(data['items'], key=lambda x: abs(x['value_1'] - x['value_2']), reverse=True)
    return data
  elif barometer == "barometer-3":
    data = {
      "id": "barometer_3",
      "label_1": excel.evaluate("'TEST_pour PROTOTYPE'!E453"),
      "label_2": excel.evaluate("'TEST_pour PROTOTYPE'!D453"),
      "items":[
        {
          "name": excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(i + 464)),
          "value_1": excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 464)),
          "value_2": excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 464))
        } for i in range(6) if excel.evaluate("'TEST_pour PROTOTYPE'!C{}".format(i + 464))
      ],
    }
    # Sort the items based on the difference between first_value and second_value
    data['items'] = sorted(data['items'], key=lambda x: abs(x['value_1'] - x['value_2']), reverse=True)
    return data
  elif barometer == "barometer-4":
    data = {
      "id": "barometer_4",
      "items": [
        {
          "category": excel.evaluate("'TEST_pour PROTOTYPE'!N{}".format(485 + i)),
          "weight": excel.evaluate("'TEST_pour PROTOTYPE'!O{}".format(485 + i)),
          "behaviors": [],
        } for i in range(7)
      ],
    }
    for item in data['items']:
      for i in range(44):
        if excel.evaluate("'TEST_pour PROTOTYPE'!AM{}".format(470 + i)) == 'à inclure' and excel.evaluate("'TEST_pour PROTOTYPE'!AJ{}".format(470 + i)) == item['category']:
          behavior = {
            "name": excel.evaluate("'TEST_pour PROTOTYPE'!AK{}".format(470 + i)),
            "weight": excel.evaluate("'TEST_pour PROTOTYPE'!AL{}".format(470 + i)) 
          }
          item['behaviors'].append(behavior)
    # Sort behaviors of each item by their weight
    for item in data['items']:
      item['behaviors'].sort(key=lambda x: x['weight'], reverse=True)
    
    # Replace behaviors with behavior values without weight
    for item in data['items']:
      item['behaviors'] = [behavior['name'] for behavior in item['behaviors']]
    return data
  elif barometer == "barometer-5":
    data = {
      "id": "barometer_5",
      "value": excel.evaluate("'TEST_pour PROTOTYPE'!C524"),
      "range": [
        {
          "name": excel.evaluate("'TEST_pour PROTOTYPE'!F{}".format(i + 525)),
          "min": excel.evaluate("'TEST_pour PROTOTYPE'!G{}".format(i + 525)),
          "max": excel.evaluate("'TEST_pour PROTOTYPE'!H{}".format(i + 525)),
        } for i in range(4)
      ] ,
    }
    for r in data['range']:
      if r['min'] <= data['value'] <= r['max']:
        data['result'] = r['name']
        break
    data['value'] = (data['value'] / data['range'][3]['max']) * 100
    data['green'] = (data['range'][0]['max'] / data['range'][3]['max']) * 100
    data['yellow'] = (data['range'][1]['max'] / data['range'][3]['max']) * 100
    data['orange'] = (data['range'][2]['max'] / data['range'][3]['max']) * 100
    return data
  elif barometer == "barometer-6":
    data = {
      "id": "barometer_6",
      "value": excel.evaluate("'TEST_pour PROTOTYPE'!C545"),
      "range": [
        excel.evaluate("'TEST_pour PROTOTYPE'!D545"), # Green
        excel.evaluate("'TEST_pour PROTOTYPE'!E545"), # Yellow (min for risk)
        excel.evaluate("'TEST_pour PROTOTYPE'!F545"), # Orange
        excel.evaluate("'TEST_pour PROTOTYPE'!G545"), # Red
        excel.evaluate("'TEST_pour PROTOTYPE'!H545"), # Max
      ]
    }
    return data
  elif barometer == "barometer-7":
    data = {
      "id": "barometer_7",
      "items": [],
    }
    for i in range(30):
      value = excel.evaluate("'TEST_pour PROTOTYPE'!E{}".format(i + 571))
      if isinstance(value, int) and value > 0:
        title = excel.evaluate("'TEST_pour PROTOTYPE'!D{}".format(i + 571))
        data['items'].append({"name": title, "value": value})
        # Maximum of 7 items
        if len(data['items']) >= 7:
          break
    data['items'] = sorted(data['items'], key=lambda d: d['value'], reverse=True)
    return data
  else:
    return {}