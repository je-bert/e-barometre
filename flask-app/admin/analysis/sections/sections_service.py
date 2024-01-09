from models import Section, Barometer, BarometerItem, Theme, Behavior
from flask import render_template, abort, request, make_response, jsonify
from database import db
from sqlalchemy import func

def find_all():
    sections = db.session.query(
      Section.id, 
      Section.is_active, 
      Section.order, 
      Section.title, 
      func.count(Barometer.id).label("barometers_count")
      )\
      .select_from(Section).outerjoin(Barometer)\
      .group_by(Section.id)\
      .all()
    return render_template('analysis/view-all-sections.html', sections = sections)


def find_one(id):
  section = Section.query\
    .filter_by(id = id)\
    .first()
  
  if not section:
    return abort(404)
  
  barometers = db.session.query(
      Barometer.section_id, 
      Barometer.id, 
      Barometer.is_active, 
      Barometer.order, 
      Barometer.title, 
      Barometer.about_barometer, 
      Barometer.type, 
      Barometer.min_result,
      Barometer.min_weight,
      func.count(Theme.id).label("themes_count")
      )\
      .select_from(Barometer).filter_by(section_id = id).outerjoin(Theme)\
      .group_by(Barometer.id)\
      .all()

  return render_template('analysis/view-all-barometers.html', section = section, barometers = barometers)

def update_one(id):
  if request.method == 'GET':
    section = Section.query\
        .filter_by(id = id)\
        .first()
  
    if not section:
      return abort(404)
    
    return render_template('analysis/update-section.html', section = section)

  data = request.form

  if not data.get('title') or not data.get('order'):
    return "Formulaire invalide.", 400

  section = Section.query\
    .filter_by(id = id)\
    .first()

  if not section:
    return "La section d'analyse n'existe pas.", 404

  section.title = data.get('title')
  section.order = data.get('order')
  section.is_active = 1 if data.get('is_active') else 0
  db.session.commit()
  
  return jsonify(section)

def add_one():
  if request.method == 'POST':
      data = request.form

      if not data.get('title'):
          return make_response("Formulaire invalide.", 400)
       
      section = Section()
      section.id = generate_new_id()
      section.title = data.get('title')
      section.order = data.get('order')
      section.is_active = 1 if data.get('is_active') else 0
      db.session.add(section)
      db.session.commit()

      return jsonify(section)

  return render_template('analysis/add-section.html')

def delete_one(id):
    section = Section.query\
        .filter_by(id = id)\
        .first()
    
    if not section:
      return make_response("L'item n'existe pas.", 404)
    
    db.session.delete(section)
    db.session.commit()
    return 'Section d\'analyse supprimée'

def generate_new_id():
  last = Section.query.order_by(Section.id.desc()).first()
  if last:
    id = int(last.id) + 1
  else:
    id = 1
  while Section.query.filter_by(id = id).first():
    id += 1
  return id