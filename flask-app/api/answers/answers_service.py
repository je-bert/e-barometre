
from flask import request, jsonify, abort
from models import User, Question, Answer
from database import db
from datetime import datetime

def update(current_user):

  user_id = current_user.user_id

  user = User.query\
    .filter_by(user_id = user_id)\
    .first()

  if not user:
      return abort(400)

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
    
    if  question:
      errors.append(f"answers[{index}]: La question avec l'identifiant {question_id} n'existe pas.")
      continue
    
    #TODO: Validation answer + custom answer

    new_answer = Answer(question_id = question_id, user_id = user_id, value = answer['value'], date_created = datetime.now())
    db.session.merge(new_answer)
    db.session.commit()

  if len(errors) > 0:
    return jsonify(errors), 200
    
  return jsonify("Vos réponses ont été sauvegardées!"), 200