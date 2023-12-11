from flask import render_template, send_file
from models import User, Report, Question, Answer, AnalysisSubsectionSubtheme, AnalysisSubsection, AnalysisSection, AnalysisSubsectionTheme, AnalysisSubsectionItem
import os
import math
from questions import questions_service

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
  
  answers = questions_service.generate_gradients(report.report_id)
  sections = []

  analysis_sections = AnalysisSection.query\
    .all()
  
  for analysis_section in analysis_sections:
    sections.append(render_template('reports/section-title.html', content = analysis_section.title))
    analysis_subsections = AnalysisSubsection.query\
      .filter_by(analysis_section_id = analysis_section.analysis_section_id)\
      .all()
    
    for analysis_subsection in analysis_subsections:
      results = []
      ranges = []
      flag_introduction = analysis_subsection.flag_introduction if analysis_subsection.flag_introduction != None else ''
      barometer = analysis_subsection.barometer
      about_barometer =analysis_subsection.about_barometer 

      themes = AnalysisSubsectionTheme.query\
        .filter_by(analysis_subsection_id = analysis_subsection.analysis_subsection_id)\
        .all()

      max = 0
      total = 0
      avg = 0

      if barometer == 'barometer-5':
        # for each theme
        for theme in themes:
          subthemes = AnalysisSubsectionSubtheme.query\
            .filter_by(analysis_subsection_theme_id = theme.analysis_subsection_theme_id)\
            .all()
          subtotal = 0
          sub_red_flags = []
          sub_yellow_flags = []
          
          for subtheme in subthemes:
            question = Question.query\
              .filter_by(question_id = subtheme.question_id)\
              .first()
            answer = answers.get(subtheme.question_id)
            answer_model = Answer.query\
              .filter_by(report_id = report.report_id , question_id = subtheme.question_id)\
              .first()
            print(question.question_id, answer, question.intensity)
            if question == None or question.question_id == 'PFA25a': #TODO: Validate this question
              max = max
            else:
              max = max + 10
            if answer == None or answer_model == None or answer_model.value == '-1' or  answer_model.value == None:
              continue
            else:
              total = total + int(answer_model.value)
            subtotal = subtotal + answer
            if subtheme.red_flag != None and subtheme.red_flag != '':
              sub_red_flags.append({"value": answer, "content":subtheme.red_flag, 'keep': subtheme.min_for_red_flag != None and answer >= subtheme.min_for_red_flag})
            if subtheme.yellow_flag != None and subtheme.yellow_flag != '':
              sub_yellow_flags.append({"value": answer, "content":subtheme.yellow_flag, 'keep': subtheme.min_for_yellow_flag != None and answer >= subtheme.min_for_yellow_flag})
          avg = avg + subtotal / len(subthemes)
          sub_avg = normal_round(subtotal / len(subthemes))
          print("sub_avg: ", sub_avg)
          sub_red_flags = [flag['content'] for flag in sub_red_flags if flag["value"] >= sub_avg or flag['keep']]
          sub_yellow_flags = [flag['content'] for flag in sub_yellow_flags if flag["value"] >= sub_avg or flag['keep']]
          results.append({"id": theme.analysis_subsection_theme_id, "avg": sub_avg, "red_flags": sub_red_flags, "yellow_flags": sub_yellow_flags})
      elif barometer == 'barometer-2' or barometer == 'barometer-3':
        for theme in themes:
          total = 0
          subthemes = AnalysisSubsectionSubtheme.query\
            .filter_by(analysis_subsection_theme_id = theme.analysis_subsection_theme_id)\
            .all()
          
          if len(subthemes) != 2:
            continue

          pfa = subthemes[0] if subthemes[0].question_id.startswith('PFA') else subthemes[1]
          pcr = subthemes[1] if subthemes[0].question_id.startswith('PFA') else subthemes[0]
          answer_1 = answers.get(pfa.question_id) if answers.get(pfa.question_id) != None else 0
          answer_2 = answers.get(pcr.question_id) if answers.get(pcr.question_id) != None else 0
          answer_model_1 = Answer.query\
              .filter_by(report_id = report.report_id , question_id = pfa.question_id)\
              .first()
          answer_model_2 = Answer.query\
              .filter_by(report_id = report.report_id , question_id = pcr.question_id)\
              .first()
          answer_model_1 = int(answer_model_1.value) if answer_model_1 != None and answer_model_1.value != None and answer_model_1.value != '-1' else 0
          answer_model_2 = int(answer_model_2.value) if answer_model_2 != None and answer_model_2.value != None and answer_model_2.value != '-1' else 0
          if answer_model_1 > total:
            total = answer_model_1
          if answer_model_2 > total:
            total = answer_model_2
          subtotal = answer_1 + answer_2
          avg = avg + subtotal
          print(answer_1, answer_2, subtotal)
          if subtotal > 0:
            ranges.append({"name": theme.name, "value_1": answer_model_2, "value_2": answer_model_1})
          results.append({"id": theme.analysis_subsection_theme_id, "avg": subtotal, "red_flags": [], "yellow_flags": []})

          
      if len(themes) > 0:
        avg = normal_round(avg / (len(themes))) # last theme removed
      print("total: ", total, "max: ", max, "avg: ", avg)

      # keep results only above average
      results = [result for result in results if result["avg"] >= avg]

      analysis = []
      observations = []
      yellow_flags = []
      red_flags = []
      ressources = []
      hide = False

      items = AnalysisSubsectionItem.query\
        .filter_by(analysis_subsection_id = analysis_subsection.analysis_subsection_id, analysis_subsection_theme_id = None)\
        .all()
      
      for item in items:
        if item.type == 'range':
          if barometer == 'barometer-5' :
            ranges.append({"name": item.content, "min": item.min, "max": item.max})
        if total >= item.min and total <= item.max:
          if item.type == 'hide':
            hide = True
            break
          elif item.type == 'observation':
            analysis.append(item.content)
          elif item.type == 'yellow_flag':
            yellow_flags.append(item.content)
          elif item.type == 'red_flag':
            red_flags.append(item.content)
          elif item.type == 'ressource':
            ressources.append(item.content)

      if hide:
        continue

      for result in results:
        if result['avg'] >= avg:
          for yellow_flag in result["yellow_flags"]:
            yellow_flags.append(yellow_flag)
          for red_flag in result["red_flags"]:
            red_flags.append(red_flag)
          subitems = AnalysisSubsectionItem.query\
            .filter_by(analysis_subsection_id = analysis_subsection.analysis_subsection_id, analysis_subsection_theme_id = result['id'])\
            .all()
          for item in subitems:
            if total >= item.min and total <= item.max:
              if item.type == 'observation':
                observations.append(item.content)
              elif item.type == 'yellow_flag':
                yellow_flags.append(item.content)
              elif item.type == 'red_flag':
                red_flags.append(item.content)
              elif item.type == 'ressource':
                red_flags.append(item.content)

      sections.append(render_template('reports/subsection-title.html', content = analysis_subsection.title))
      sections.append(render_template('reports/about-barometer.html', content = about_barometer))
      if barometer == 'barometer-1' or barometer == 'barometer-5' or barometer == 'barometer-6':
        # For barometer 1, 5 and 6, about barometer section is different on desktop
        sections.pop()
        sections.append(render_template('reports/about-barometer.html', content = about_barometer, hide_lg = True))
    
      if barometer == 'barometer-5' or barometer == 'barometer-2' or barometer == 'barometer-3':
        sections.append(render_template("reports/report-1/" + barometer + ".html", data = generate_barometer_data(barometer, total, ranges), about = about_barometer))

      sections.append(render_template('reports/themes.html', analysis_items = analysis, observations = observations))
      if len(red_flags) > 0 or len(yellow_flags) > 0:
        sections.append(render_template('reports/flags.html', yellow_flags = yellow_flags, red_flags = red_flags, flag_introduction = flag_introduction))
      if len(ressources) > 0:
        sections.append(render_template('reports/ressources.html', content = ressources))

  return render_template('reports/report-1/base.html', children = sections)

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
  elif barometer == "barometer-5":
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