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

  if not data.get('title'):
    return make_response("Forumulaire invalide.", 400)

  question = Question.query\
        .filter_by(question_id = id)\
        .first()

  if not question:
    return make_response("La question n'existe pas.", 404)

  question.title = data.get('title')
  db.session.commit()
  return jsonify(question)