from surveys import Survey
from questions import Question
from flask import render_template, abort

def find_all():
  surveys = Survey.query.all()
  return render_template('surveys.html', surveys = surveys)

def find_one(id):
  survey = Survey.query\
        .filter_by(survey_id = id)\
        .first()
  questions = Question.query\
        .filter_by(survey_id = id)\
        .all()
  
  if not survey:
    return abort(404)
  
  return render_template('survey.html', survey = survey, questions = questions)