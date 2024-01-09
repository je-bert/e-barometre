from models import Behavior, Question, Theme
from flask import render_template, abort, request, make_response, jsonify
from database import db

def update_one(id):
  if request.method == 'GET':
    behavior = Behavior.query\
        .filter_by(id = id)\
        .first()
  
    if not behavior:
      return abort(404)

    questions = Question.query\
      .all()
    
    return render_template('analysis/update-behavior.html', behavior = behavior, questions=questions)

  data = request.form

  if not data.get('question_id') or not data.get('ranges'):
    return "Formulaire invalide.", 400

  behavior = Behavior.query\
        .filter_by(id = id)\
        .first()

  if not behavior:
    return "Le sous-thème n'existe pas.", 404
  
  behavior.question_id = data.get('question_id')
  behavior.ranges = data.get('ranges')
  behavior.is_active = 1 if data.get('is_active') else 0
  behavior.weight = data.get('weight') if data.get('weight') else 0
  behavior.intensity = data.get('intensity') if data.get('intensity') else 0
  db.session.commit()
  return jsonify(behavior)

def add_one(id):
  if request.method == 'POST':
      data = request.form

      behavior = Behavior()
      behavior.id = generate_new_id()
      behavior.theme_id = id
      behavior.question_id = data.get('question_id')
      behavior.ranges = data.get('ranges')
      behavior.is_active = 1 if data.get('is_active') else 0
      behavior.weight = data.get('weight') if data.get('weight') else 0
      behavior.intensity = data.get('intensity') if data.get('intensity') else 0
      db.session.add(behavior)
      db.session.commit()
      return jsonify(behavior)

  questions = Question.query\
    .all()
  
  theme = Theme.query\
    .filter_by(id = id)\
    .first()

  return render_template('analysis/add-behavior.html', theme = theme, questions = questions)

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