from models import Section, Barometer, BarometerItem, Theme, Behavior 
from flask import render_template, abort, request, make_response, jsonify
from database import db

def find_one(id):
  theme = Theme.query\
    .filter_by(id = id)\
    .first()
  
  if not theme:
    return abort(404)
  
  behaviors = Behavior.query\
    .filter_by(theme_id = id)\
    .all()
  
  return render_template('analysis/view-one-theme.html', theme = theme, behaviors = behaviors)

def update_one(id):
  if request.method == 'GET':
    theme = Theme.query\
        .filter_by(id = id)\
        .first()
  
    if not theme:
      return abort(404)
    
    return render_template('analysis/update-theme.html', theme = theme)

  data = request.form

  if not data.get('title'):
    return "Formulaire invalide.", 400

  theme = Theme.query\
        .filter_by(id = id)\
        .first()

  if not theme:
    return "Le thème n'existe pas.", 404
  
  theme.name = data.get('title')
  theme.is_active = 1 if data.get('is_active') else 0
  db.session.commit()
  return jsonify(theme)

def add_one(id):
  if request.method == 'POST':
      data = request.form

      theme = Theme()
      theme.id =generate_new_id() 
      theme.barometer_id = id 
      theme.name = data.get('title')
      theme.is_active = 1 if data.get('is_active') else 0
      
      db.session.add(theme)
      db.session.commit()
      return jsonify(theme)

  barometer = Barometer.query\
    .filter_by(id = id)\
    .first()

  return render_template('analysis/add-theme.html', barometer = barometer)

def delete_one(id):
  item = Theme.query\
    .filter_by(id = id)\
    .first()

  if not item:
    return make_response("L'item n'existe pas.", 404)

  db.session.delete(item)
  db.session.commit()
  return jsonify(item)


def generate_new_id():
  last = Theme.query.order_by(Theme.id.desc()).first()
  if last:
    id = int(last.id) + 1
  else:
    id = 1
  while Theme.query.filter_by(id = id).first():
    id += 1
  return id