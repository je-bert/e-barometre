from models import Barometer, BarometerItem, Theme, Behavior, Section
from flask import render_template, abort, request, make_response, jsonify
from database import db
from sqlalchemy import func

def find_one(id):
  barometer = Barometer.query\
    .filter_by(id = id)\
    .first()
  
  if not barometer:
    return abort(404)
  
  items = BarometerItem.query\
    .filter_by(barometer_id = id)\
    .all()
  
  themes = db.session.query(
      Theme.id, 
      Theme.barometer_id, 
      Theme.is_active, 
      Theme.name, 
      func.count(Behavior.id).label("behaviors_count")
      )\
      .select_from(Theme).filter_by(barometer_id = id).outerjoin(Behavior)\
      .group_by(Theme.id)\
      .all()

  return render_template('analysis/view-one-barometer.html',barometer = barometer, items = items, themes = themes)

def update_one(id):
  if request.method == 'GET':
    barometer = Barometer.query\
        .filter_by(id = id)\
        .first()
  
    if not barometer:
      return abort(404)
    
    return render_template('analysis/update-barometer.html', barometer = barometer)

  data = request.form

  if not data.get('title') or not data.get('about_barometer') or not data.get('order') or not data.get('schema_type'):
    return "Formulaire invalide.", 400

  barometer = Barometer.query\
      .filter_by(id = id)\
      .first()

  if not barometer:
    return "La section d'analyse n'existe pas.", 404

  barometer.title = data.get('title')
  barometer.about_barometer = data.get('about_barometer')
  barometer.order = data.get('order')
  barometer.min_result = float(data.get('min_result')) if data.get('min_result') else 0
  barometer.min_weight = float(data.get('min_weight')) if data.get('min_weight') else 0
  barometer.schema_type = data.get('schema_type') if data.get('schema_type') else None
  barometer.is_active = 1 if data.get('is_active') else 0
  db.session.commit()
  return jsonify(barometer)

def add_one(id):
  if request.method == 'POST':
      data = request.form


      barometer = Barometer()
      barometer.id = generate_new_id() 
      barometer.section_id = id
      barometer.title = data.get('title')
      barometer.about_barometer = data.get('about_barometer')
      barometer.order = data.get('order') #TODO what should be the default value for order?
      barometer.type = data.get('schema_type') if data.get('schema_type') else None
      barometer.is_active = 1 if data.get('is_active') else 0
      barometer.min_result = float(data.get('min_result')) if data.get('min_result') else 0
      barometer.min_weight = float(data.get('min_weight')) if data.get('min_weight') else 0
      
      db.session.add(barometer)
      db.session.commit()
      return jsonify(barometer)

  section = Section.query\
    .filter_by(id = id)\
    .first()

  return render_template('analysis/add-barometer.html', section = section)

def delete_one(id):
  barometer = Barometer.query\
    .filter_by(id = id)\
    .first()

  if not barometer:
    return make_response("L'item n'existe pas.", 404)

  db.session.delete(barometer)
  db.session.commit()
  return jsonify(barometer)

def generate_new_id():
  last = Barometer.query.order_by(Barometer.id.desc()).first()
  if last:
    id = int(last.id) + 1
  else:
    id = 1
  while Barometer.query.filter_by(id = id).first():
    id += 1
  return id