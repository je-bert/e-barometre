from models import Barometer, BarometerItem, Theme , Behavior
from flask import render_template, abort, request, make_response, jsonify
from database import db

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
    
    behaviors = []
    for theme in themes:
      behaviors += Behavior.query\
        .filter_by(theme_id = theme.id)\
        .all()
      
    link_to_choices = [{'id': None, 'name': 'Baromètre', 'type': 'none'}]
    current_link_to = link_to_choices[0]

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

    ranges = BarometerItem.query\
      .filter_by(barometer_id = item.barometer_id, type = 'range')\
      .all()
    
    return render_template('analysis/update-item.html', item = item, link_to_choices = link_to_choices, current_link_to = current_link_to, ranges = ranges)

  data = request.form

  if not data.get('content') or not data.get('min') or not data.get('max'):
    return "Formulaire invalide.", 400

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
  item.min = float(data.get('min'))
  item.max = float(data.get('max'))
  item.is_active = 1 if data.get('is_active') else 0
  db.session.commit()
  
  return jsonify(item)

def add_one(id, type = None):
  if request.method == 'POST':
      data = request.form

      if not data.get('content') or not data.get('min') or not data.get('max') or not data.get('type'):
        return make_response("Formulaire invalide.", 400)
      
       
      item = BarometerItem()
      item.id = generate_new_id() 
      item.barometer_id =  id
      item.content = data.get('content')
      if data.get('link_to_choice') != None:
        link_to_choice = data.get('link_to_choice').split(",")
        item.theme_id = link_to_choice[1] if link_to_choice[0] == 'theme' else None
        item.behavior_id = link_to_choice[1] if link_to_choice[0] == 'behavior' else None
      item.min = float(data.get('min'))
      item.max = float(data.get('max'))
      if(item.min > item.max):  
        return make_response("Minimum et maximum invalides. Le minimum ne peut pas être plus grand que le maximum. " + item.min + " <= " + item.max, 400)
      item.type = data.get('type')
      item.is_active = 1 if data.get('is_active') else 0
      db.session.add(item)
      db.session.commit()

      return jsonify(item)
  else:
    themes = Theme.query\
        .filter_by(barometer_id = id)\
        .all()
      
    behaviors = []
    for theme in themes:
      behaviors += Behavior.query\
        .filter_by(theme_id = theme.id)\
        .all()
    link_to_choices = [{'id': None, 'name': 'Baromètre', 'type': 'none'}]

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

    barometer = Barometer.query\
      .filter_by(id = id)\
      .first()

    ranges = BarometerItem.query\
      .filter_by(barometer_id = id, type = 'range')\
      .all()

    return render_template('analysis/add-item.html', barometer = barometer, link_to_choices = link_to_choices, type = type, ranges = ranges)

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