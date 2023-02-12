from models import Survey, Question
from flask import render_template, abort, request, make_response, jsonify
from database import db

def find_all():
  surveys = Survey.query.all()
  return render_template('surveys.html', surveys = surveys)

def find_one(id):
  survey = Survey.query\
        .filter_by(survey_id = id)\
        .first()
  
  if not survey:
    return abort(404)

  questions = Question.query\
        .filter_by(survey_id = id)\
        .all()
  
  return render_template('survey.html', survey = survey, questions = questions)


def update_one(id):
  if request.method == 'GET':
    survey = Survey.query\
        .filter_by(survey_id = id)\
        .first()
  
    if not survey:
      return abort(404)
    
    return render_template('update-survey.html', survey = survey)

  data = request.form

  if not data.get('name') or not data.get('description') or not data.get('color') or not data.get('cover_picture_url'):
    return make_response("Forumulaire invalide.", 400)

  survey = Survey.query\
        .filter_by(survey_id = id)\
        .first()

  if not survey:
    return make_response("Le questionnaire n'existe pas.", 404)

  survey.name = data.get('name')
  survey.description = data.get('description')
  survey.color = data.get('color')
  survey.cover_picture_url = data.get('cover_picture_url')
  survey.status = 'inactive' if not data.get('status') else 'active'
  db.session.commit()
  return jsonify(survey)
