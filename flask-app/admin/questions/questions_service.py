from models import Question
from flask import render_template, abort, request, make_response, jsonify
from database import db


def update_one(id):
  if request.method == 'GET':
    question = Question.query\
        .filter_by(question_id = id)\
        .first()
  
    if not question:
      return abort(404)
    
    return render_template('update-question.html', question = question)

  data = request.form

  if not data.get('title') or not data.get('order'):
    return make_response("Formulaire invalide.", 400)

  question = Question.query\
        .filter_by(question_id = id)\
        .first()

  if not question:
    return make_response("La question n'existe pas.", 404)

  question.intro = data.get('intro') if data.get('intro') else None
  question.title = data.get('title')
  question.info_bubble_text = data.get('info_bubble_text') if data.get('info_bubble_text') else None
  question.condition = data.get('condition') if data.get('condition') else None
  intensity = data.get('intensity')
  question.intensity = int(intensity) if intensity and intensity.isdigit() else None
  question.conditional_intensity = data.get('conditional_intensity') if data.get('conditional_intensity') else None
  order = data.get('order')
  question.order = int(order) if order and order.isdigit() else None
  question.active = 0 if not data.get('active') else 1
  question.violence_related = 0 if not data.get('violence_related') else 1
  if question.type == 'integer':
    min_value = data.get('min_value')
    question.min_value = int(min_value) if min_value and min_value.isdigit() else None
    max_value = data.get('max_value')
    question.max_value = int(max_value) if max_value and max_value.isdigit() else None
  ladderC = data.get('ladderC')
  question.ladderC = int(ladderC) if ladderC and ladderC.isdigit() else None
  ladderE = data.get('ladderE')
  question.ladderE = int(ladderE) if ladderE and ladderE.isdigit() else None
  ladderV = data.get('ladderV')
  question.ladderV = int(ladderV) if ladderV and ladderV.isdigit() else None
  question.parent = data.get('parent') if data.get('parent') else None
  question.red_flag = None #TODO: Is it a string?
  db.session.commit()
  return jsonify(question)

def add_one(id):
  survey_id = id

  if request.method == 'POST':
      data = request.form

      if not data.get('value') or not data.get('label') or not data.get('order'):
        return make_response("Formulaire invalide.", 400)

      question = Question()
      question.question_id = data.get('question_id') # TODO add verification for regex, to match it with the right survey id letter start
      question.intro = data.get('intro') if data.get('intro') else None
      question.title = data.get('title')
      question.info_bubble_text = data.get('info_bubble_text') if data.get('info_bubble_text') else None
      question.condition = data.get('condition') if data.get('condition') else None
      intensity = data.get('intensity')
      question.intensity = int(intensity) if intensity and intensity.isdigit() else None
      question.conditional_intensity = data.get('conditional_intensity') if data.get('conditional_intensity') else None
      order = data.get('order')
      question.order = int(order) if order and order.isdigit() else None
      question.active = 0 if not data.get('active') else 1
      question.violence_related = 0 if not data.get('violence_related') else 1
      if question.type == 'integer':
        min_value = data.get('min_value')
        question.min_value = int(min_value) if min_value and min_value.isdigit() else None
        max_value = data.get('max_value')
        question.max_value = int(max_value) if max_value and max_value.isdigit() else None
      ladderC = data.get('ladderC')
      question.ladderC = int(ladderC) if ladderC and ladderC.isdigit() else None
      ladderE = data.get('ladderE')
      question.ladderE = int(ladderE) if ladderE and ladderE.isdigit() else None
      ladderV = data.get('ladderV')
      question.ladderV = int(ladderV) if ladderV and ladderV.isdigit() else None
      question.parent = data.get('parent') if data.get('parent') else None
      question.red_flag = None #TODO: Is it a string?

      db.session.add(question)
      db.session.commit()

      return jsonify(question)

  return render_template('add-question.html',survey_id = survey_id, question_id = question.question_id)

def delete_one(id):
    question = Question.query\
        .filter_by(question_id = id)\
        .first()
    
    if not question:
      return make_response("La question n'existe pas.", 404)
  
    db.session.delete(question)
    db.session.commit()
    return jsonify(question)
