from models import Choice, Label, Answer, CustomAnswer, Survey, Question
from flask import abort, jsonify

def find_all():
  surveys = Survey.query\
        .filter_by(status= 'active')\
        .all()

  if not surveys:
    return abort(400, 'Record not found') 

  return jsonify(surveys), 200

def find_one(id):
  survey = Survey.query\
        .filter_by(survey_id = id, status = 'active')\
        .first()

  if not survey:
    return abort(404)

  questions = Question.query\
        .filter_by(survey_id = id)\
        .all()

  res = jsonify(survey).json
  res['questions'] = jsonify(questions).json

  for question in res['questions']:
    choices = []
    if question['type'] == 'labeled-ladder':
      choices = Label.query\
        .filter_by(label_id = question['label_id'])\
        .all()
    else:
      choices = Choice.query\
        .filter_by(question_id = question['question_id'])\
        .all()
    if len(choices) > 0:
      question['choices'] = jsonify(choices).json

    #TODO: real user_id
    answer = Answer.query\
        .filter_by(question_id = question['question_id'], user_id = 0)\
        .first()

    if answer != None:
      question['answer'] = answer.value
      if 'custom' in answer.value:
        #TODO: real user_id
        custom_answer = CustomAnswer.query\
          .filter_by(question_id = question['question_id'], user_id = 0)\
          .first()
        if custom_answer != None:
          question['custom_answer'] = custom_answer.value
  return res, 200