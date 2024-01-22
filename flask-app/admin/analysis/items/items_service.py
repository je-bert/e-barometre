from models import Barometer, BarometerItem, Theme , Behavior, Indicator
from flask import render_template, abort, request, make_response, jsonify
from database import db
from utils import condition_parser as cp

def update_one(id):
  if request.method == 'GET':
    item = BarometerItem.query\
        .filter_by(id = id)\
        .first()
  
    if not item:
      return abort(404)
    
    themes = Theme.query\
      .filter_by(barometer_id = item.barometer_id)\
      .all()

    indicators = Indicator.query\
      .filter_by(barometer_id = item.barometer_id)\
      .all()
    
    behaviors = []
    for theme in themes:
      behaviors += Behavior.query\
        .filter_by(theme_id = theme.id)\
        .all()
    
    barometer = Barometer.query\
      .filter_by(id = item.barometer_id)\
      .first()
    
    if not barometer:
      return abort(404)
      
    link_to_choices = [{'id': None, 'name': 'Baromètre', 'type': 'none'}] if barometer.type != 'action-reaction' else []
    current_link_to = None

    if barometer.type != 'action-reaction':
      for theme in themes:
        link_to_choices.append({
          'id': theme.id,
          'name': "Thème " + (theme.name if theme.name else 'sans nom'),
          'type': 'theme'
        })
        if int(theme.id) == item.theme_id:
          current_link_to = link_to_choices[-1]
      for behavior in behaviors:
        link_to_choices.append({
          'id': behavior.id,
          'name': "Comportement " + behavior.question_id,
          'type': 'behavior'
        })
        if int(behavior.id) == item.behavior_id:
          current_link_to = link_to_choices[-1]
    else:
      for indicator in indicators:
        link_to_choices.append({
          'id': str(indicator.id),
          'name': "Indicateur " + str(indicator.content),
          'type': 'indicator'
        })
        if int(indicator.id) == item.indicator_id:
          current_link_to = link_to_choices[-1]
        for theme in themes:
          link_to_choices.append({
            'id': str(indicator.id) + ',' + str(theme.id),
            'name': "Indicateur " + str(indicator.content) + " - Thème " + (theme.name if theme.name else 'sans nom'),
            'type': 'indicator+theme'
          })
          if int(theme.id) == item.theme_id and item.indicator_id == indicator.id:
            current_link_to = link_to_choices[-1]
        for behavior in behaviors:
          link_to_choices.append({
            'id': str(indicator.id) + ',' + str(behavior.id),
            'name': "Indicateur " + str(indicator.content) + " - Comportement " + behavior.question_id,
            'type': 'indicator+behavior'
          })
          if int(behavior.id) == item.behavior_id and item.indicator_id == indicator.id:
            current_link_to = link_to_choices[-1]

    ranges = BarometerItem.query\
      .filter_by(barometer_id = item.barometer_id, type = 'range')\
      .all()
    
    
    return render_template('analysis/update-item.html', item = item, link_to_choices = link_to_choices, current_link_to = current_link_to, ranges = ranges)

  data = request.form

  if not data.get('content') or not data.get('min') or not data.get('max'):
    return "Formulaire invalide.", 400

  if data.get('condition') != None and data.get('condition') != '':
    if not cp.is_valid_condition_syntax(data.get('condition')):
      return make_response("La condition n'est pas valide.", 400)
      

  item = BarometerItem.query\
      .filter_by(id = id)\
      .first()

  if not item:
    return "L'item n'existe pas.", 404
  
  item.content = data.get('content')
  if data.get('link_to_choice') != None:
    link_to_choice = data.get('link_to_choice').split(",")
    item.theme_id = link_to_choice[1] if link_to_choice[0] == 'theme' else None
    item.behavior_id = link_to_choice[1] if link_to_choice[0] == 'behavior' else None
    item.indicator_id = link_to_choice[1] if link_to_choice[0] == 'indicator' else None
    if link_to_choice[0] == 'indicator+theme':
      item.theme_id = link_to_choice[2]
      item.indicator_id = link_to_choice[1]
    if link_to_choice[0] == 'indicator+behavior':
      item.behavior_id = link_to_choice[2]
      item.indicator_id = link_to_choice[1]
  item.min = float(data.get('min'))
  item.max = float(data.get('max'))
  if(item.min > item.max):  
    return make_response("Minimum et maximum invalides. Le minimum ne peut pas être plus grand que le maximum. " + str(item.min) + " <= " + str(item.max), 400)
  item.is_active = 1 if data.get('is_active') else 0
  item.is_unavoidable = 1 if data.get('is_unavoidable') else 0
  item.condition = None if data.get('condition') == '' else data.get('condition')
  db.session.commit()
  
  return jsonify(item)

def add_one(id, type = None, indicator_id = None):
  if request.method == 'POST':
      data = request.form

      if not data.get('content') or not data.get('min') or not data.get('max') or not data.get('type'):
        return make_response("Formulaire invalide.", 400)
      
      if data.get('condition') != None and data.get('condition') != '':
        if not cp.is_valid_condition_syntax(data.get('condition')):
          return make_response("La condition n'est pas valide.", 400)
      
       
      item = BarometerItem()
      item.id = generate_new_id() 
      item.barometer_id =  id
      item.indicator_id = data.get('indicator_id') if data.get('indicator_id') else None
      item.content = data.get('content')
      if data.get('link_to_choice') != None:
        link_to_choice = data.get('link_to_choice').split(",")
        item.theme_id = link_to_choice[1] if link_to_choice[0] == 'theme' else None
        item.behavior_id = link_to_choice[1] if link_to_choice[0] == 'behavior' else None
        item.indicator_id = link_to_choice[1] if link_to_choice[0] == 'indicator' else None
        if link_to_choice[0] == 'indicator+theme':
          item.theme_id = link_to_choice[2]
          item.indicator_id = link_to_choice[1]
        if link_to_choice[0] == 'indicator+behavior':
          item.behavior_id = link_to_choice[2]
          item.indicator_id = link_to_choice[1]
      item.min = float(data.get('min'))
      item.max = float(data.get('max'))
      if(item.min > item.max):  
        return make_response("Minimum et maximum invalides. Le minimum ne peut pas être plus grand que le maximum. " + str(item.min) + " <= " + str(item.max), 400)
      item.type = data.get('type')
      item.is_active = 1 if data.get('is_active') else 0
      item.is_unavoidable = 1 if data.get('is_unavoidable') else 0
      item.condition = None if data.get('condition') == '' else data.get('condition')
      db.session.add(item)
      db.session.commit()

      return jsonify(item)
  else:
    themes = Theme.query\
        .filter_by(barometer_id = id)\
        .all()
    
    indicators = Indicator.query\
      .filter_by(barometer_id = id)\
      .all()
      
    behaviors = []

    for theme in themes:
      behaviors += Behavior.query\
        .filter_by(theme_id = theme.id)\
        .all()
    barometer = Barometer.query\
      .filter_by(id = id)\
      .first()
    
    if not barometer:
      return abort(404)
    
    link_to_choices = [{'id': None, 'name': 'Baromètre', 'type': 'none'}] if barometer.type != 'action-reaction' else []

    if barometer.type != 'action-reaction':
      for theme in themes:
        link_to_choices.append({
          'id': theme.id,
          'name': "Thème " + (theme.name if theme.name else 'sans nom'),
          'type': 'theme'
        })
      for behavior in behaviors:
        link_to_choices.append({
          'id': behavior.id,
          'name': "Comportement " + behavior.question_id,
          'type': 'behavior'
        })
    else:
      for indicator in indicators:
        link_to_choices.append({
          'id': str(indicator.id),
          'name': "Indicateur " + str(indicator.content),
          'type': 'indicator'
        })
        for theme in themes:
          link_to_choices.append({
            'id': str(indicator.id) + ',' + str(theme.id),
            'name': "Indicateur " + str(indicator.content) + " - Thème " + (theme.name if theme.name else 'sans nom'),
            'type': 'indicator+theme'
          })
        for behavior in behaviors:
          link_to_choices.append({
            'id': str(indicator.id) + ',' + str(behavior.id),
            'name': "Indicateur " + str(indicator.content) + " - Comportement " + behavior.question_id,
            'type': 'indicator+behavior'
          })
    

    ranges = BarometerItem.query\
      .filter_by(barometer_id = id, type = 'range')\
      .all()

    return render_template('analysis/add-item.html', barometer = barometer, link_to_choices = link_to_choices, type = type, ranges = ranges, indicator_id = int(indicator_id) if indicator_id else None)

def delete_one(id):
    item = BarometerItem.query\
        .filter_by(id = id)\
        .first()
    
    if not item:
      return make_response("L'item n'existe pas.", 404)
    
    db.session.delete(item)
    db.session.commit()
    return 'Item supprimé'


def generate_new_id():
  last = BarometerItem.query.order_by(BarometerItem.id.desc()).first()
  if last:
    id = int(last.id) + 1
  else:
    id = 1
  while BarometerItem.query.filter_by(id = id).first():
    id += 1
  return id