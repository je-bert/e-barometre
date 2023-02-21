from models import Survey, Question
from flask import render_template, abort, request, make_response, jsonify
from database import db
from werkzeug.utils import secure_filename
import os

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

  if not data.get('name') or not data.get('description') or not data.get('color'):
    return make_response("Forumulaire invalide.", 400)

  survey = Survey.query\
        .filter_by(survey_id = id)\
        .first()

  if not survey:
    return make_response("Le questionnaire n'existe pas.", 404)

  # Update cover picture
  if 'cover_picture_file' in request.files:
    file = request.files['cover_picture_file']
    if file:
      file.filename = "{}.{}".format(survey.survey_id, secure_filename(file.filename.split('.')[-1]))
      filename = os.path.join('static/img/survey_covers/', file.filename)
      os.makedirs(os.path.dirname(filename), exist_ok=True)
      file.save(filename)
      survey.cover_picture_url = '/' + filename
  
  #TODO: Can we remove cover picture?

  survey.name = data.get('name')
  survey.description = data.get('description')
  survey.color = data.get('color')
  survey.status = 'inactive' if not data.get('status') else 'active'
  db.session.commit()
  return jsonify(survey)
