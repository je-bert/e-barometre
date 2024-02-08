from flask import render_template, send_file
from models import User, Report, Question, Answer, Section, Barometer, BarometerItem, Theme, Behavior, BarometerActor, Actor, Indicator
import os
from questions import questions_service
from utils import condition_parser as cp

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
  is_admin = True # TODO: Look if the user to fetch report is admin
  report = Report.query\
    .filter_by(report_id = id)\
    .first()

  if not report:
    return "Not found", 404
  
  intensity_dict = questions_service.generate_gradients(id)
  answers_dict = {answer.question_id: answer for answer in Answer.query\
    .filter_by(report_id = id)\
    .all()}
  report_sections = []
  other_considerations_section = {
    "title": "Considérations importantes",
    "about": "Dans cette section, nous abordons des aspects cruciaux qui n'ont pas trouvé leur place dans les sections précédentes du rapport, mais qui demeurent essentiels à considérer.",
    "flag_introduction": None,
    "analysis" : [],
    "observations": [],
    "yellow_flags": [],
    "red_flags": [],
    "ressources": [],
    "hide": False
  }

  sections = Section.query\
    .filter_by(is_active = True)\
    .all()
  
  for section in sections:
    report_sections.append(render_template('reports/section-title.html', content = section.title))

    barometers = Barometer.query\
      .filter_by(section_id = section.id, is_active = True)\
      .all()
    
    for barometer in barometers:
      generate_barometer(barometer, report_sections, other_considerations_section, answers_dict, intensity_dict, is_admin)

  report_sections += generate_report_section(other_considerations_section)

  return render_template('reports/report-1/base.html', children = report_sections)


def generate_barometer(barometer, report_sections, other_considerations_section, answers_dict, intensity_dict, is_admin):
  current_section = {
    "title": barometer.title,
    "about": barometer.about_barometer,
    "flag_introduction": None,
    "analysis" : [],
    "observations": [],
    "yellow_flags": [],
    "red_flags": [],
    "ressources": [],
    "data": {},
    "hide": False
  }
  
  if barometer.type == 'action-reaction':
    generate_action_reaction_results(barometer, current_section, report_sections, other_considerations_section, answers_dict, intensity_dict, is_admin)
  elif barometer.type == 'mirror':
    generate_mirror_results(barometer, current_section, report_sections, other_considerations_section, answers_dict, intensity_dict, is_admin)
  elif barometer.type == 'linear-gauge' or barometer.type == 'circular-gauge':
    generate_gauge_results(barometer, current_section, report_sections, other_considerations_section, answers_dict, intensity_dict, is_admin)
  else:
    current_section['hide'] = True
  report_sections += generate_report_section(current_section, barometer)
  
def generate_gauge_results(barometer, current_section,report_sections, other_considerations_section, answers_dict, intensity_dict, is_admin):
  results = {}
  themes = Theme.query\
    .filter_by(barometer_id = barometer.id, is_active = True)\
    .all()
  for theme in themes:
    behaviors = Behavior.query\
      .filter_by(theme_id = theme.id, is_active = True)\
      .all()
    for behavior in behaviors:
      ranges = behavior.ranges.split(',')
      is_desc = ranges[0].split(':')[0] > ranges[-1].split(':')[1]

      answer = None
      if behavior.question_id in answers_dict:
        answer = answers_dict.get(behavior.question_id)
      
      if answer == None or answer.value == None or answer.value == '-1':
          if behavior.question_id in intensity_dict and answer != None and answer.value == '-1': # -1 means the question was s/o, but was shown to the user
            results[behavior.id] = {"answer": answer.value if answer != None else answer,"question_id": behavior.question_id, "theme_id": theme.id, "result": 0, "intensity": intensity_dict[behavior.question_id], "weight": behavior.weight, "ignore": True}
      else:
        col = 0
        answer = int(answer.value)
        while (col < len(ranges)):
          current_range = ranges[col].split(':')
          if (len(current_range) != 2):
            continue
          if (answer >= int(current_range[0]) and answer <= int(current_range[1]) or (is_desc and answer <= int(current_range[0]) and answer >= int(current_range[1]))):
            break
          col = col + 1
        
        if (col == len(ranges)):
          continue
        if (is_desc):
          result =  0.25  * col + 0.25 * (int(current_range[0]) - answer) / (int(current_range[0]) - int(current_range[1]) + 1)
        else:
          result =  0.25 * col + 0.25 * (answer - int(current_range[0])) / (int(current_range[1]) - int(current_range[0]) + 1)
        if (col == len(ranges) - 1 and answer == int(current_range[1])):
          result = 1
        results[behavior.id] = {"answer": answer, "question_id": behavior.question_id,  "theme_id": theme.id, "result": result, "intensity": intensity_dict[behavior.question_id] if behavior.question_id in intensity_dict else 0, "weight": behavior.weight, "ignore": False}

  max_weight = 0
  answered_weight = 0
  max_score = 0
  score = 0
  results_by_theme_id = {}
  ranges = []
  if is_admin:
    report_sections.append('<div class="border w-[80%] border-blue-500"><h3 class="text-center mt-6">{}</h3>'.format(barometer.title))
    report_sections.append('<table class="w-full admin-table">')
    report_sections.append('<tr><th class="text-left">Comportement</th><th class="text-center">Réponse</th><th class="text-center">Intensité</th><th class="text-center">Poids</th><th class="text-center">Indice</th></tr>')
  for result in results.values():
    max_weight = max_weight + result['weight']
    answered_weight = answered_weight + (0 if result['ignore'] else result['weight'])
    max_score = (max_score + result['intensity']) if result['ignore'] == False else max_score
    score = score + (0 if result['ignore'] else result['intensity'] * result['result'])
    results_by_theme_id[result['theme_id']] = results_by_theme_id.get(result['theme_id'], [])
    results_by_theme_id[result['theme_id']].append(0 if result['ignore'] else  result['result'])
    if is_admin:
      report_sections.append('<tr><td>{}</td><td class="text-center">{}</td><td class="text-center">{}</td><td class="text-center">{}</td><td class="text-center">{}</td></tr>'.format(result['question_id'], result['answer'], result['intensity'], round(result['weight'],3), round(result['result'] * result['intensity'], 3)))
  if is_admin:
    report_sections.append('</table>')

  avg_by_theme_id = {}
  for theme_id in results_by_theme_id:
    avg = 0
    for result in results_by_theme_id[theme_id]:
      avg = avg + result
    avg = safe_division(avg, len(results_by_theme_id[theme_id]))
    avg_by_theme_id[theme_id] = avg
  barometer_avg = 0
  for theme_id in avg_by_theme_id:
    barometer_avg = barometer_avg + avg_by_theme_id[theme_id]
  barometer_avg = safe_division(barometer_avg, len(avg_by_theme_id))
  hide = False

  total = safe_division(score, max_score)
  weight_percentage = safe_division(answered_weight, max_weight)
  if is_admin:
    report_sections.append('<p class="text-center mt-6">Résultat: {} / {} = {}</p>'.format(round(score, 3), round(max_score, 3), round(total, 3)))
    report_sections.append('<p class="text-center">Poids répondu: {} / {} = {}</p></div>'.format(round(answered_weight, 3), round(max_weight, 3), round(weight_percentage, 3)))
  if total < barometer.min_result or weight_percentage < barometer.min_weight:
    if barometer.min_weight_note != None and weight_percentage < barometer.min_weight:
      report_sections.append(render_template('reports/subsection-title.html', content = barometer.title))
      report_sections.append(render_template('reports/note.html', content = barometer.min_weight_note)) 
    elif barometer.min_result_note != None and total < barometer.min_result:
      report_sections.append(render_template('reports/subsection-title.html', content = barometer.title))
      report_sections.append(render_template('reports/note.html', content = barometer.min_result_note))
    hide = True

  items = BarometerItem.query\
    .filter_by(barometer_id = barometer.id, is_active = True)\
    .all()

  for item in items:
    value = total
    if item.condition != None and item.condition != '':
      if not cp.parse_condition(item.condition, answers_dict):
        continue
    if item.behavior_id != None and str(item.behavior_id) in results:
      value = results[str(item.behavior_id)]['result']
      #if result['ignore'] == False and (result['intensity'] * result['result']) >= avg_by_theme_id[result['theme_id']] and avg_by_theme_id[result['theme_id']] >= barometer_avg
    elif item.theme_id != None and str(item.theme_id) in avg_by_theme_id:
      value = avg_by_theme_id[str(item.theme_id)]
    if item.type == 'range':
      if barometer.type == 'linear-gauge' or barometer.type == 'circular-gauge':
        if hide == False:
          ranges.append({"name": item.content, "min": float(item.min), "max": float(item.max)})
    if value >= item.min and (value < item.max if item.max != 1 else value <= item.max):
      if item.type == 'observation':
        if item.theme_id == None and item.behavior_id == None:
          if hide and item.is_unavoidable:
            other_considerations_section['analysis'].append(item.content)
          else:
            current_section['analysis'].append(item.content)
        else:
          if hide and item.is_unavoidable:
            other_considerations_section['observations'].append(item.content)
          else:
            current_section['observations'].append(item.content)
      elif item.type == 'yellow_flag':
        if hide and item.is_unavoidable:
          other_considerations_section['yellow_flags'].append(item.content)
        else:
          current_section['yellow_flags'].append(item.content)
      elif item.type == 'red_flag':
        if hide and item.is_unavoidable:
          other_considerations_section['red_flags'].append(item.content)
        else:
          current_section['red_flags'].append(item.content)
      elif item.type == 'flag_introduction':
          current_section['flag_introduction'] = item.content
      elif item.type == 'ressource':
        if hide and item.is_unavoidable:
          other_considerations_section['ressources'].append(item.content)
        else:
          current_section['ressources'].append(item.content)
  if not hide:
    current_section['data'] = {"value": total, "ranges": ranges}
  else:
    current_section['hide'] = True
  return current_section
  
def generate_mirror_results(barometer, current_section,report_sections, other_considerations_section, answers_dict, intensity_dict, is_admin):
  hide = False # TODO: Implement hide depending on results or weight
  behavior_results = {}
  results = {}
  themes = Theme.query\
        .filter_by(barometer_id = barometer.id, is_active = True)\
        .all()
  actors = BarometerActor.query\
    .filter_by(barometer_id = barometer.id)\
    .join(Actor, Actor.id == BarometerActor.actor_id)\
    .add_columns(Actor.name, BarometerActor.id)\
    .all()

  if len(actors) != 2:
    return current_section

  current_section['data'] = {'items': [], 'actor_1': actors[0].name, 'actor_2': actors[1].name}
  for theme in themes:
    behaviors = Behavior.query\
      .filter_by(theme_id = theme.id, is_active = True)\
      .all()
    
    if len(behaviors) != 2:
      results[theme.id] ={"name": theme.name,'actor_1': None, 'actor_2': None }
      continue

    actor_1 = behaviors[0] if behaviors[0].actor_id == actors[0].id else (behaviors[1].actor_id if behaviors[1].actor_id == actors[0].id else None)
    actor_2 = behaviors[1] if behaviors[1].actor_id == actors[1].id else (behaviors[0].actor_id if behaviors[0].actor_id == actors[1].id else None)

    if actor_1 == None or actor_2 == None or actor_1.actor_id == None or actor_2.actor_id == None or actor_1.actor_id == actor_2.actor_id:
      results[theme.id] = {"name": theme.name,'actor_1': None, 'actor_2': None , 'result': 0 }
      continue

    actor_1.answer = answers_dict.get(actor_1.question_id) if answers_dict.get(actor_1.question_id) != None else None
    actor_2.answer = answers_dict.get(actor_2.question_id) if answers_dict.get(actor_2.question_id) != None else None

    if actor_1.answer == None or actor_2.answer == None or actor_1.answer.value == '-1' or actor_2.answer.value == '-1':
      results[theme.id] = {"name": theme.name,'actor_1': None, 'actor_2': None, 'result': 0 }
      continue
    else:
      actor_1.answer = int(actor_1.answer.value)
      actor_2.answer = int(actor_2.answer.value)
      actor_1.intensity = intensity_dict[actor_1.question_id]
      actor_2.intensity = intensity_dict[actor_2.question_id]
      actor_1.score = actor_1.answer * intensity_dict[actor_1.question_id]
      actor_2.score = actor_2.answer * intensity_dict[actor_2.question_id]
      actor_1.max_score = actor_1.intensity * 10
      actor_2.max_score = actor_2.intensity * 10
      theme_result = safe_division(actor_1.score + actor_2.score, actor_1.max_score + actor_2.max_score)

    difference = actor_1.score + actor_2.score

    behavior_results[behaviors[0].id] = actor_1.answer
    behavior_results[behaviors[1].id] = actor_2.answer

    results[theme.id] = {"name": theme.name, "actor_1": actor_1, "actor_2": actor_2, 'result': theme_result }
    if difference > 0:
      current_section['data']['items'].append({"name": theme.name, "value_1": actor_1.answer, "value_2": actor_2.answer,'result': theme_result  })

  # max_weight = 0
  # answered_weight = 0
  score = 0
  max_score = 0
  if is_admin:
    report_sections.append('<div class="border w-[80%] border-blue-500"><h3 class="text-center mt-6">{}</h3>'.format(barometer.title))
    report_sections.append('<table class="w-full admin-table">')
    report_sections.append('<tr><th class="text-left">Thème</th><th class="text-center">{}</th><th class="text-center">{}</th><th class="text-center">Écart</th></tr>'.format(current_section['data']['actor_1'], current_section['data']['actor_2']))
  for result in results.values():
    # max_weight = max_weight + result['weight']
    # answered_weight = answered_weight + (0 if result['ignore'] else result['weight'])
    if is_admin:
      if result['actor_1'] != None and result['actor_2'] != None:
        sum_score = result['actor_1'].score + result['actor_2'].score
        score = score + sum_score
        sum_max_score = result['actor_1'].max_score + result['actor_2'].max_score
        max_score = max_score + sum_max_score
        report_sections.append('<tr><td>{}</td><td class="text-center">{} x {} = {}</td><td class="text-center">{} x {} = {}</td><td class="text-center">{} / {} = {}</td></tr>'.format(result['name'], result['actor_1'].answer, result['actor_1'].intensity,result['actor_1'].score, result['actor_2'].answer, result['actor_2'].intensity,result['actor_2'].score, sum_score, sum_max_score, round(result['result'], 3)))
      else:
        report_sections.append('<tr><td>{}</td><td class="text-center">-1</td><td class="text-center">-1</td><td class="text-center">-</td></tr>'.format(result['name']))
  if is_admin:
    report_sections.append('</table>')

  total = safe_division(score, max_score)
  if is_admin:
    report_sections.append('<p class="text-center mt-6">Résultat: {} / {} = {}</p></div>'.format(round(score, 3), round(max_score, 3), round(total, 3)))

  items = BarometerItem.query\
    .filter_by(barometer_id = barometer.id, is_active = True)\
    .all()

  for item in items:
    value = total
    if item.condition != None and item.condition != '':
      if not cp.parse_condition(item.condition, answers_dict):
        continue
    if item.behavior_id != None:
      if str(item.behavior_id) in behavior_results:
        value = (behavior_results[str(item.behavior_id)] / 10)
      else: 
        continue
    elif item.theme_id != None:
      if str(item.theme_id) in results and results[str(item.theme_id)]['actor_1'] != None and results[str(item.theme_id)]['actor_2'] != None:
        value = safe_division((results[str(item.theme_id)]['actor_1'].score + results[str(item.theme_id)]['actor_2'].score) , (results[str(item.theme_id)]['actor_1'].max_score + results[str(item.theme_id)]['actor_2'].max_score))
      else: 
        continue
    if value >= item.min and (value < item.max if item.max != 1 else value <= item.max):
      if item.type == 'observation':
        if item.theme_id == None and item.behavior_id == None:
          if hide and item.is_unavoidable:
            other_considerations_section['analysis'].append(item.content)
          else:
            current_section['analysis'].append(item.content)
        else:
          if hide and item.is_unavoidable:
            other_considerations_section['observations'].append(item.content)
          else:
            current_section['observations'].append(item.content)
      elif item.type == 'yellow_flag':
        if hide and item.is_unavoidable:
          other_considerations_section['yellow_flags'].append(item.content)
        else:
          current_section['yellow_flags'].append(item.content)
      elif item.type == 'red_flag':
        if hide and item.is_unavoidable:
          other_considerations_section['red_flags'].append(item.content)
        else:
          current_section['red_flags'].append(item.content)
      elif item.type == 'flag_introduction':
          current_section['flag_introduction'] = item.content
      elif item.type == 'ressource':
        if hide and item.is_unavoidable:
          other_considerations_section['ressources'].append(item.content)
        else:
          current_section['ressources'].append(item.content)
  return current_section

def generate_action_reaction_results(barometer, current_section,report_sections, other_considerations_section, answers_dict, intensity_dict, is_admin):
  current_section['data'] = {"indicators": [], "items":[]}
  results = {}
  themes = Theme.query\
    .filter_by(barometer_id = barometer.id, is_active = True)\
    .all()
  for theme in themes:
    behaviors = Behavior.query\
      .filter_by(theme_id = theme.id, is_active = True)\
      .all()
    
    indicators = Indicator.query\
      .filter_by(barometer_id = barometer.id)\
      .all()
    results[theme.id] = {"name": theme.name, "behaviors": [], "ranges": [{"PF": {"value":0, "max":0, "min":0}, "PC": {"value":0, "max":0, "min":0},"NC": {"value":0, "max":0, "min":0}, "E":{"value":0, "max":0, "min":0}} for i in range(len(indicators))]}
    for behavior in behaviors:
      ranges = behavior.ranges.split(',')
      if len(ranges) != len(indicators):
        continue
      intensity = intensity_dict[behavior.question_id] if behavior.question_id in intensity_dict else 0
      answer = answers_dict.get(behavior.question_id) if answers_dict.get(behavior.question_id) != None else None
      if answer != None:
        answer = int(answer.value)
      results[theme.id]['behaviors'].append({'question_id': behavior.question_id, 'answer': answer, 'intensity': intensity, 'ranges': behavior.ranges, 'is_action': behavior.actor_id == 5, 'weight': behavior.weight})
    
  if is_admin:
    report_sections.append('<div class="border w-[80%] border-blue-500"><h3 class="text-center mt-6">{}</h3>'.format(barometer.title))
    report_sections.append('<table class="w-full admin-table">')
    report_sections.append('<tr><th class="text-left">Thème</th><th class="text-center">Comportement</th><th class="text-center">Acteur</th><th class="text-center">Fréquence x Intensité x Poids</th>')
    for indicator in indicators:
      report_sections.append('<th class="text-center">{}</th>'.format(indicator.content))
    report_sections.append('</tr>')
  for result in results.values():
    for b in result['behaviors']:
      if is_admin:
        ranges = b['ranges'].split(',')
        if b['answer'] != None and b['answer'] != -1:
          report_sections.append('<tr><td></td><td class="text-center">{}</td><td class="text-center">{}</td><td class="text-center">{} x {} x {} = {}</td>'.format(b['question_id'], "Action" if b['is_action'] else "Réaction", b['answer'], b['intensity'], b['weight'], b['answer'] * b['weight'] * (b['intensity'] if b['intensity'] != None else 0)))
          col = 0
          while (col < len(ranges)):
            current_range = ranges[col].split(':')
            score = 0
            if b['answer'] >= int(current_range[0]):
              symbol = 'V'
              # score = safe_division(b['answer'] - int(current_range[0]) + 1, int(current_range[1]) - int(current_range[0]) + 1)
              indice = (b['answer'] if b['answer'] < int(current_range[1]) else int(current_range[1])) * b['intensity'] * b['weight']
              max = b['intensity'] * int(current_range[1]) * b['weight']
              min = b['intensity'] * int(current_range[0]) * b['weight']
              if b['is_action']:
                if indice > result['ranges'][col][b['question_id'][0:2]]['value']:
                  result['ranges'][col][b['question_id'][0:2]]['value'] = indice
                if max > result['ranges'][col][b['question_id'][0:2]]['max']:
                  result['ranges'][col][b['question_id'][0:2]]['max'] = max
                if min > result['ranges'][col][b['question_id'][0:2]]['min']:
                  result['ranges'][col][b['question_id'][0:2]]['min'] = min
              else:
                if indice > result['ranges'][col][b['question_id'][0]]['value']:
                  result['ranges'][col][b['question_id'][0]]['value'] = indice
                if max > result['ranges'][col][b['question_id'][0]]['max']:
                  result['ranges'][col][b['question_id'][0]]['max'] = max 
                if min > result['ranges'][col][b['question_id'][0]]['min']:
                  result['ranges'][col][b['question_id'][0]]['min'] = min 
            else:
              symbol = 'F'
              # score = 0
              indice = 0
            report_sections.append('<td class="text-center {}">{}: {}</td>'.format( "opacity-50" if symbol == 'F' else '',symbol, ranges[col]))
            col = col + 1
        else:
          report_sections.append('<tr><td></td><td class="text-center">{}</td><td class="text-center">{}</td><td class="text-center">-1</td>'.format( b['question_id'], "Action" if b['is_action'] else "Réaction"))
          for i in range(len(indicators)):
            report_sections.append('<td class="text-center opacity-50">F: {}</td>'.format(ranges[i]))
        report_sections.append('</tr>')
    report_sections.append('<tr class="font-bold"><td>{}</td><td></td><td></td><td></td>'.format(result['name']))
    for i in range(len(indicators)):
      value = sum(value['value'] for value in result['ranges'][i].values())
      reaction = 'V' if result['ranges'][i]['E']['value'] > 0 else 'F'
      action = 'V' if value - result['ranges'][i]['E']['value'] > 0 else 'F'
      if i == 0 and action == 'V' and reaction == 'V':
        current_section['data']['items'].append({"name": result['name'], "value": value})
      max = sum(value['max'] for value in result['ranges'][i].values())
      min = sum(value['min'] for value in result['ranges'][i].values())
      report_sections.append('<td class="text-center">({}|{}){} < {} < {} ({})</td>'.format(action, reaction,round(min,2),round(value,2), round(max,2), round(safe_division(value - min + 1, max - min + 1) if value != 0 else 0,2)))
      
  if is_admin:    
    report_sections.append('</tr></table>')
    for i in range(len(indicators)):
      ranges = []
      value = 0
      min = 0
      max = 0
      items = BarometerItem.query\
      .filter_by(barometer_id = barometer.id, is_active = True, type = 'range', indicator_id = indicators[i].id)\
      .all()
      for item in items:
        ranges.append({"name": item.content, "min": float(item.min), "max": float(item.max)})
        print (item.content)
      for result in results.values():
        value += sum(value['value'] for value in result['ranges'][i].values())
        max += sum(value['max'] for value in result['ranges'][i].values())
        min += sum(value['min'] for value in result['ranges'][i].values())
      current_section['data']['indicators'].append({"value": safe_division(value - min + 1, max - min + 1) if value != 0 else 0, "ranges": ranges, "id": indicators[i].id, "content": indicators[i].content})
      report_sections.append('<p class="text-center mt-6">Résultat {}: {} < {} < {} ({})</p>'.format(indicators[i].content, round(min,2),round(value,2), round(max,2), round(safe_division(value - min + 1, max - min + 1) if value != 0 else 0,2)))
    report_sections.append('</div>')
    

  return current_section


def generate_report_section(content, barometer = None):
  if barometer == None and len(content['analysis']) == 0 and len(content['observations']) == 0 and len(content['yellow_flags']) == 0 and len(content['red_flags']) == 0 and len(content['ressources']) == 0 or content['hide'] == True:
    return []
  report_sections = []
  report_sections.append(render_template('reports/subsection-title.html', content = content['title']))
  report_sections.append(render_template('reports/about-barometer.html', content = content['about']))
  if barometer != None:
    if barometer.type == 'linear-gauge' or barometer.type == 'circular-gauge':
      # About barometer section is different on desktop for these barometers
      report_sections.pop()
      report_sections.append(render_template('reports/about-barometer.html', content = content['about'], hide_lg = True))
    report_sections.append(render_template("reports/report-1/" + barometer.type + ".html", data = generate_barometer_data(barometer.id, barometer.type, content['data']), about = content['about']))
  report_sections.append(render_template('reports/themes.html', analysis_items = content['analysis'], observations = content['observations']))
  report_sections.append(render_template('reports/flags.html', yellow_flags = content['yellow_flags'], red_flags = content['red_flags'], flag_introduction = content['flag_introduction']))
  report_sections.append(render_template('reports/ressources.html', content = content['ressources']))
  return report_sections

def generate_barometer_data(id, barometer, content):
  if barometer == "linear-gauge":
    return generate_linear_gauge_data(id, content)
  elif barometer == "circular-gauge":
    return generate_circular_gauge_data(id, content)
  elif barometer == "mirror":
    return generate_mirror_data(id, content)
  elif barometer == "action-reaction":
    return generate_action_reaction_data(id, content)
  else:
    return {}
  
def generate_linear_gauge_data(id, content):
  indicator = Indicator.query\
    .filter_by(barometer_id = id)\
    .first()
  data = {
    "id": id,
    "value": content['value'],
    "content": indicator.content if indicator != None else "Indicateur",
    "range": content['ranges'] ,
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

def generate_circular_gauge_data(id, content):
  indicator = Indicator.query\
    .filter_by(barometer_id = id)\
    .first()
  data = {
    "id": 'circular-'+id,
    "value": content['value'],
    "content": indicator.content if indicator != None else "Indicateur",
    "range": [
      content['ranges'][0]['min'], # Green
      content['ranges'][1]['min'], # Yellow (min for risk)
      content['ranges'][2]['min'], # Orange
      content['ranges'][3]['min'], # Red
      content['ranges'][3]['max'], # Max
    ]
  }
  for r in content['ranges']:
    if r['min'] <= data['value'] <= r['max']:
      data['result'] = r['name']
      break
  return data

def generate_action_reaction_data(id, content):
  data = {
      "id": id,
      "indicators": [],
      "items": content['items']
    }
  data['items'] = sorted(data['items'], key=lambda d: d['value'], reverse=True)
  data['items'] = data['items'][0:7] # take the 7 first items
  for indicator in content['indicators']:
    temp = {
      "id": 'action-reaction-' + data['id'] + "-" + str(indicator['id']),
      "value": indicator['value'],
      "content": indicator['content'],
      "range": [
        indicator['ranges'][0]['min'], # Green
        indicator['ranges'][1]['min'], # Yellow (min for risk)
        indicator['ranges'][2]['min'], # Orange
        indicator['ranges'][3]['min'], # Red
        indicator['ranges'][3]['max'], # Max
      ]}
    for r in indicator['ranges']:
      if r['min'] <= temp['value'] <= r['max']:
        temp['result'] = r['name']
        break
    data['indicators'].append(temp)
  return data
  
def generate_mirror_data(id, content):
  data = {
    "id": id,
    "label_1": content['actor_1'],
    "label_2": content['actor_2'],
    "items": content['items']
  }
  data['items'] = sorted(data['items'], key=lambda x: x['result'], reverse=True)
  for item in data['items']:
    item['color'] = get_mirror_data_color(item['result'])
  return data

def get_mirror_data_color(value):
  if value < 0.25:
    return "1"
  elif value < 0.5:
    return "2"
  elif value < 0.75:
    return "3"
  else:
    return "4"

def safe_division(a, b):
  return a / (b if b != 0 else 1)