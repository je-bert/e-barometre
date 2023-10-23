from flask import request, jsonify, abort
from models import User, Question, Answer,UserSurvey, Report, CustomAnswer
from database import db
from datetime import datetime

def update(current_user):

  user_id = current_user.user_id

  user = User.query\
    .filter_by(user_id = user_id)\
    .first()

  if not user:
      return abort(400)
  
  report = Report.query\
      .filter_by(user_id = user_id, is_completed = False)\
      .first()
    
  if report == None:
    return jsonify({"message":"Aucun rapport en cours."}), 400
  
  if request.method == 'DELETE':

    completed_surveys = UserSurvey.query\
      .filter_by(report_id = report.report_id)\
      .all()

    answers = Answer.query\
      .filter_by(report_id = report.report_id)\
      .all()

    for survey in completed_surveys:
      db.session.delete(survey)
  
    for answer in answers:
      db.session.delete(answer)

    db.session.delete(report)
    
    db.session.commit()

    return jsonify("Vos réponses ont été supprimées!"), 200

  json = request.json

  if not 'answers' in json:
    return "Erreur: le champ 'answers' est absent.", 400
  
  errors = []

  for index, answer in enumerate(json['answers']):
    if not 'question_id' in answer:
      errors.append(f"answers[{index}]: Le champ 'question_id' est manquant dans l'une des réponses.")
      continue

    if not 'value' in answer:
      errors.append(f"answers[{index}]: Le champ 'value' est absent dans l'une des réponses.")
      continue

    question_id = answer['question_id']

    question = Question.query\
        .filter_by(question_id = question_id)\
        .first()
    
    if not question:
      errors.append(f"answers[{index}]: La question avec l'identifiant {question_id} n'existe pas.")
      continue
    
    #TODO: Validation answer

    new_answer = Answer(question_id = question_id, report_id = report.report_id, value = answer['value'], date_created = datetime.now())
    db.session.merge(new_answer)
    
    if 'custom_value' in answer:
      custom_answer = CustomAnswer(question_id = question_id, report_id = report.report_id, value = answer['custom_value'], date_created = datetime.now())
      db.session.merge(custom_answer)
    else:
      CustomAnswer.query\
        .filter_by(question_id = question_id, report_id = report.report_id)\
        .delete()
      

    db.session.commit()

  if len(errors) > 0:
    return jsonify(errors), 200
  
  answers = Answer.query\
    .filter_by(report_id = report.report_id)\
    .all()

  if not answers:
    return abort(404)
    
  return jsonify(answers), 200

def find_one(current_user, question_id):
  user_id = current_user.user_id

  user = User.query\
    .filter_by(user_id = user_id)\
    .first()

  if not user:
      return abort(400)
  
  report = Report.query\
    .filter_by(user_id = user_id, is_completed = False)\
    .first()
    
  if report == None:
    return jsonify({"message":"Aucun rapport en cours."}), 400
  
  answer = Answer.query\
    .filter_by(report_id = report.report_id, question_id = question_id)\
    .first()
  
  if not answer:
    return abort(404)
  
  return jsonify(answer), 200

def find_all(current_user):
  user_id = current_user.user_id

  user = User.query\
    .filter_by(user_id = user_id)\
    .first()

  if not user:
      return abort(400)

  report = Report.query\
    .filter_by(user_id = user_id, is_completed = False)\
    .first()
    
  if report == None:
    return jsonify({"message":"Aucun rapport en cours."}), 400
  
  answers = Answer.query\
    .filter_by(report_id = report.report_id)\
    .all()
  
  custom_answers = CustomAnswer.query\
    .filter_by(report_id = report.report_id)\
    .all()
  
  custom_dict = {}

  for custom_answer in custom_answers:
    custom_dict[custom_answer.question_id] = custom_answer
  
  res = []

  for answer in answers:
    item = {
      'question_id': answer.question_id,
      'value': answer.value,
      'report_id': answer.report_id,
      
    }
    if custom_dict.get(answer.question_id):
      item['custom_value'] = custom_dict.get(answer.question_id).value

    res.append(item)
  

  if not answers:
    return abort(404)
  
  return res, 200