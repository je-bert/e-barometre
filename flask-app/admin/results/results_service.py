from flask import render_template, send_file
from models import User, Report, Question, Answer, Section, Barometer, BarometerItem, Theme, Behavior
import os
import math

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


def find_one_auto(id):
  report = Report.query\
    .filter_by(report_id = id)\
    .first()
  
  if not report:
    return "Not found", 404
  
  report_sections = []

  sections = Section.query\
    .filter_by(is_active = True)\
    .all()
  
  for section in sections:
    report_sections.append(render_template('reports/section-title.html', content = section.title))

    barometers = Barometer.query\
      .filter_by(section_id = section.id, is_active = True)\
      .all()
    
    for barometer in barometers:
      results = {}
      ranges = []
      flag_introduction = None

      themes = Theme.query\
        .filter_by(barometer_id = barometer.id, is_active = True)\
        .all()

      if barometer.type == 'jauge':
        # for each theme
        for theme in themes:
          behaviors = Behavior.query\
            .filter_by(theme_id = theme.id, is_active = True)\
            .all()
          for behavior in behaviors:
            ranges = behavior.ranges.split(',')

            answer = Answer.query\
              .filter_by(report_id = report.report_id , question_id = behavior.question_id)\
              .first()
            
            if answer == None or  answer.value == None or answer.value == '-1':
               results[behavior.id] = {"theme_id": theme.id, "result": 0, "intensity": behavior.intensity, "weight": behavior.weight, "ignore": True}
            else:
              col = 0
              answer = int(answer.value)
              while (col < len(ranges)):
                current_range = ranges[col].split(':')
                if (len(current_range) != 2):
                  continue
                if (answer >= int(current_range[0]) and answer <= int(current_range[1])):
                  break
                col = col + 1
              
              if (col == len(ranges)):
                continue
              result = 0.25 * col + 0.25 * (answer - int(current_range[0])) / (int(current_range[1]) - int(current_range[0]) + 1)
              if (col == len(ranges) - 1 and answer == int(current_range[1])):
                result = 1
              results[behavior.id] = { "theme_id": theme.id, "result": result, "intensity": behavior.intensity, "weight": behavior.weight, "ignore": False}
      else: continue
      max_weight = 0
      answered_weight = 0
      max_score = 0
      score = 0
      results_by_theme_id = {}
      for result in results.values():
        max_weight = max_weight + result['weight']
        answered_weight = answered_weight + (0 if result['ignore'] else result['weight'])
        max_score = (max_score + result['intensity']) if result['ignore'] == False else max_score
        score = score + (0 if result['ignore'] else result['intensity'] * result['result'])
        results_by_theme_id[result['theme_id']] = results_by_theme_id.get(result['theme_id'], [])
        results_by_theme_id[result['theme_id']].append(score)

      avg_by_theme_id = {}
      for theme_id in results_by_theme_id:
        avg = 0
        for result in results_by_theme_id[theme_id]:
          avg = avg + result
        avg = avg / len(results_by_theme_id[theme_id])
        avg_by_theme_id[theme_id] = avg
      barometer_avg = 0
      for theme_id in avg_by_theme_id:
        barometer_avg = barometer_avg + avg_by_theme_id[theme_id]
      barometer_avg = barometer_avg / len(avg_by_theme_id)
      print( "answered: ", answered_weight, "/", max_weight, "result: ", score, "/", max_score, score / max_score)

      if score / max_score < barometer.min_result or answered_weight / max_weight < barometer.min_weight:
        # hide the section
        continue

      total = score / max_score
      analysis = []
      observations = []
      yellow_flags = []
      red_flags = []
      ressources = []
      ranges = []

      items = BarometerItem.query\
        .filter_by(barometer_id = barometer.id, is_active = True)\
        .all()

      for item in items:
        value = total
        if item.behavior_id != None and str(item.behavior_id) in results:
          value = results[str(item.behavior_id)]['result']
          #if result['ignore'] == False and (result['intensity'] * result['result']) >= avg_by_theme_id[result['theme_id']] and avg_by_theme_id[result['theme_id']] >= barometer_avg
        elif item.theme_id != None and str(item.theme_id) in avg_by_theme_id:
          value = avg_by_theme_id[str(item.theme_id)]
        if item.type == 'range':
          if barometer.type == 'jauge':
            ranges.append({"name": item.content, "min": float(item.min), "max": float(item.max)})
        if value >= item.min and (value < item.max if item.max != 1 else value <= item.max):
          if item.type == 'observation':
            analysis.append(item.content)
          elif item.type == 'yellow_flag':
            yellow_flags.append(item.content)
          elif item.type == 'red_flag':
            red_flags.append(item.content)
          elif item.type == 'flag_introduction':
            flag_introduction = item.content
          elif item.type == 'ressource':
            ressources.append(item.content)

      report_sections.append(render_template('reports/subsection-title.html', content = barometer.title))
      report_sections.append(render_template('reports/about-barometer.html', content = barometer.about_barometer))
      if barometer.type == 'barometer-1' or barometer.type == 'jauge' or barometer.type == 'barometer-6':
        # For barometer 1, 5 and 6, about barometer section is different on desktop
        report_sections.pop()
        report_sections.append(render_template('reports/about-barometer.html', content = barometer.about_barometer, hide_lg = True))
    
      if barometer.type == 'jauge' or barometer.type == 'barometer-2' or barometer.type == 'barometer-3':
        report_sections.append(render_template("reports/report-1/" + barometer.type + ".html", data = generate_barometer_data(barometer.type, total, ranges), about = barometer.about_barometer))

      report_sections.append(render_template('reports/themes.html', analysis_items = analysis, observations = observations))
      if len(red_flags) > 0 or len(yellow_flags) > 0:
        report_sections.append(render_template('reports/flags.html', yellow_flags = yellow_flags, red_flags = red_flags, flag_introduction = flag_introduction))
      if len(ressources) > 0:
        report_sections.append(render_template('reports/ressources.html', content = ressources))

  return render_template('reports/report-1/base.html', children = report_sections)

def generate_barometer_data(barometer, value, content):
  if barometer == "barometer-2" or barometer == "barometer-3":
    data = {
      "id": barometer,
      "label_1": "PARENT RÉPONDANT",
      "label_2": "CO PARENT",
      "items": content,
    }
    print(data['items'])
    # Sort the items based on the difference between first_value and second_value
    data['items'] = sorted(data['items'], key=lambda x: abs((int(x['value_1']) if x['value_1'] != None else 0) - (int(x['value_2']) if x['value_2'] != None else 0)), reverse=True)
    return data
  elif barometer == "jauge":
    data = {
      "id": "barometer_5",
      "value": value,
      "range": content ,
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
  else:
    return {}

def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)