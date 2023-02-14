
from flask import request, jsonify, abort
from models import User
from database import db
from datetime import datetime
from shutil import copyfile
import os
from openpyxl import load_workbook

def update(current_user):
  json = request.json

  #TODO: Code for real db answers save
  # if not 'answers' in json:
  #   return "Erreur", 400

  # for answer in json['answers']:
  #   if not 'question_id' in answer:
  #     return "Erreur", 400

  #   if not 'value' in answer:
  #     return "Erreur", 400

  #   question = Question.query\
  #       .filter_by(question_id = answer['question_id'])\
  #       .first()
    
  #   if not question:
  #     return "Erreur", 400
    
  #   ##TODO: Validation answer + custom answer

  #   row = Answer(question_id = answer['question_id'], user_id = current_user.user_id, value = answer['value'], date_created = datetime.now())
  #   db.session.merge(row)
  #   db.session.commit()

  user = User.query\
    .filter_by(user_id = current_user.user_id)\
    .first()

  if not user:
      return abort(400)

  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  template_file = 'b_results_template.xlsx'
  output_file = 'master_results/{}_{}_{}.xlsx'.format(user.first_name, user.last_name, datetime.now().strftime('%Y_%m_%d_%H%M%S'))
  copyfile(template_file, output_file)

  # Load the workbook and access the sheet we'll paste into
  wb = load_workbook(output_file)
  ws = wb['TEST_pour application']

  for i in range(4, 33):
    ws['B' + str(i)] = "0" #TODO: Real values

  wb.save(output_file)
    
  return jsonify("Vos réponses ont été sauvegardées!"), 200