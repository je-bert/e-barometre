from models import Behavior, Question, Theme, BarometerItem,BarometerActor ,Actor, Indicator,Barometer
from flask import render_template, abort, request, make_response, jsonify
from database import db

def update_one(id):
  behavior = Behavior.query\
      .filter_by(id = id)\
      .first()
  
  if not behavior:
    return abort(404)

  theme = Theme.query\
    .filter_by(id = behavior.theme_id)\
    .first()
  
  barometer = Barometer.query\
    .filter_by(id = theme.barometer_id)\
    .first()
  
  if not barometer:
    return make_response("Le baromètre n'existe pas.", 400)
  
  if barometer.type == 'action-reaction':
    ranges = Indicator.query\
      .filter_by(barometer_id = theme.barometer_id)\
      .all()
  else:
    ranges = BarometerItem.query\
      .filter_by(barometer_id = theme.barometer_id, type = 'range')\
      .all()
    ranges.sort(key=lambda x: x.min) 

  actors = BarometerActor.query\
    .filter_by(barometer_id = theme.barometer_id)\
    .all()

  if request.method == 'GET':
    
    questions = Question.query\
      .all()
    
    current_ranges = []
    if behavior.ranges != None:
      for i in behavior.ranges.split(','):
        print(i)
        current_ranges.append({
          'min': i.split(':')[0],
          'max': i.split(':')[1]
        })
        if len(current_ranges) >= len(ranges):
          break
    
    while len(current_ranges) < len(ranges):
      current_ranges.append({
        'min': '0',
        'max': '0'
      })

    for actor in actors:
      item = Actor.query\
        .filter_by(id = actor.actor_id)\
        .first()
      if item:
        actor.name = item.name
    return render_template('analysis/update-behavior.html', behavior = behavior, questions=questions, ranges = ranges, current_ranges = current_ranges, actors = actors)

  data = request.form

  if not data.get('question_id'):
    return "Formulaire invalide.", 400
  
  is_ascendant = None
  previous = None

  ranges_str_builder = []
  for range in ranges:
    min_str = data.get('range-' +  str(range.id) + '-min')
    max_str = data.get('range-' +  str(range.id) + '-max')
    if min_str != None and max_str != None:
      min = int(min_str)
      max = int(max_str)
      if previous != min and barometer.type != 'action-reaction':
        if previous != None:
          if is_ascendant == None:
            is_ascendant = previous < min
          elif is_ascendant != (previous < min):
            return make_response("Échelle invalide: elle doit être soit ascendante, soit descendante. " + str(previous) + (' > ' if is_ascendant else ' < ') + str(min), 400)
      if len(ranges_str_builder) > 0:
        ranges_str_builder.append(',')
      if min != max:
        if is_ascendant == None:
          is_ascendant =  min < max
        elif is_ascendant != None and is_ascendant != (min < max):
          return make_response("Échelle invalide: elle doit être soit ascendante, soit descendante. " + str(min) + (' > ' if is_ascendant else ' < ') + str(max), 400)
      ranges_str_builder.append(min_str + ':' + max_str)
      previous = max
    else:
      return make_response("Échelle invalide", 400)

  actor = None
  if len(actors) > 0:
    if data.get('actor') == None or data.get('actor') == '':
      return make_response("Vous devez sélectionner un acteur.", 400)
    actor = BarometerActor.query\
      .filter_by(id = data.get('actor'), barometer_id = theme.barometer_id)\
      .first()
    if not actor:
      return make_response("L'acteur sélectionné n'existe pas.", 400)
  
  behavior.question_id = data.get('question_id')
  behavior.ranges = ''.join(ranges_str_builder)
  behavior.is_active = 1 if data.get('is_active') else 0
  behavior.weight = data.get('weight') if (data.get('weight') and data.get('weight').replace(".", "").isnumeric()) else 0
  behavior.actor_id = actor.id if actor else None
  db.session.commit()
  return jsonify(behavior)

def add_one(id):
    
  theme = Theme.query\
    .filter_by(id = id)\
    .first()
  
  barometer = Barometer.query\
    .filter_by(id = theme.barometer_id)\
    .first()
  
  if not barometer:
    return make_response("Le baromètre n'existe pas.", 400)
  

  if barometer.type == 'action-reaction':
    ranges = Indicator.query\
      .filter_by(barometer_id = theme.barometer_id)\
      .all()
  else:
    ranges = BarometerItem.query\
      .filter_by(barometer_id = theme.barometer_id, type = 'range')\
      .all()
    ranges.sort(key=lambda x: x.min)

  actors = BarometerActor.query\
    .filter_by(barometer_id = theme.barometer_id)\
    .all()
  
  if request.method == 'POST':
      data = request.form
      is_ascendant = None
      previous = None

      ranges_str_builder = []
      for range in ranges:
        min_str = data.get('range-' +  range.id + '-min')
        max_str = data.get('range-' +  range.id + '-max')
        if min_str != None and max_str != None:
          min = int(min_str)
          max = int(max_str)
          if previous != min and barometer.type != 'action-reaction':
            if previous != None:
              if is_ascendant == None:
                is_ascendant = previous < min
              elif is_ascendant != (previous < min):
                return make_response("Échelle invalide: elle doit être soit ascendante, soit descendante. " + str(previous) + (' > ' if is_ascendant else ' < ') + str(min), 400)
          if len(ranges_str_builder) > 0:
            ranges_str_builder.append(',')
          if min != max:
            if is_ascendant == None:
              is_ascendant =  min < max
            elif is_ascendant != None and is_ascendant != (min < max):
              return make_response("Échelle invalide: elle doit être soit ascendante, soit descendante. " + str(min) + (' > ' if is_ascendant else ' < ') + str(max), 400)
          ranges_str_builder.append(min_str + ':' + max_str)
          previous = max
        else:
          return make_response("Échelle invalide", 400)
        
      actor = None
      if len(actors) > 0:
        if data.get('actor') == None or data.get('actor') == '':
          return make_response("Vous devez sélectionner un acteur.", 400)
        actor = BarometerActor.query\
          .filter_by(id = data.get('actor'), barometer_id = theme.barometer_id)\
          .first()
        if not actor:
          return make_response("L'acteur sélectionné n'existe pas.", 400)
  
      behavior = Behavior()
      behavior.id = generate_new_id()
      behavior.theme_id = id
      behavior.question_id = data.get('question_id')
      behavior.ranges = ''.join(ranges_str_builder)
      behavior.is_active = 1 if data.get('is_active') else 0
      behavior.weight = data.get('weight') if (data.get('weight') and data.get('weight').isdigit()) else 0
      behavior.actor_id = actor.id if actor else None
      db.session.add(behavior)
      db.session.commit()
      return jsonify(behavior)

  for actor in actors:
    item = Actor.query\
      .filter_by(id = actor.actor_id)\
      .first()
    if item:
      actor.name = item.name

  questions = Question.query\
    .all()

  return render_template('analysis/add-behavior.html', theme = theme, questions = questions, ranges = ranges, actors = actors)

def delete_one(id):
  item = Behavior.query\
    .filter_by(id = id)\
    .first()

  if not item:
    return make_response("L'item n'existe pas.", 404)

  db.session.delete(item)
  db.session.commit()
  return jsonify(item)

def generate_new_id():
  last = Behavior.query.order_by(Behavior.id.desc()).first()
  if last:
    id = int(last.id) + 1
  else:
    id = 1
  while Behavior.query.filter_by(id = id).first():
    id += 1
  return id