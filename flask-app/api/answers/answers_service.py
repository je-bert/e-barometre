
from flask import request, jsonify, abort
from models import User, Question, Answer
from database import db
from datetime import datetime
from shutil import copyfile
import os
from openpyxl import load_workbook

def update(current_user):

  user = User.query\
    .filter_by(user_id = current_user.user_id)\
    .first()

  if not user:
      return abort(400)

  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  template_file = 'master_results_template.xlsx'
  output_file = 'master_results/{}.xlsx'.format(user.user_id)
  if not os.path.exists(output_file):
    copyfile(template_file, output_file)

  # Load the workbook and access the sheet we'll paste into
  wb = load_workbook(output_file)

  # Demo code
  ws = wb['TEST_pour application']

  json = request.json

  if not 'answers' in json:
    return "Erreur", 400

  for answer in json['answers']:
    if not 'question_id' in answer:
      return "Erreur", 400

    if not 'value' in answer:
      return "Erreur", 400

    question = Question.query\
        .filter_by(question_id = answer['question_id'])\
        .first()
    
    if not question:
      return "Erreur", 400
    
    ##TODO: Validation answer + custom answer

    new_answer = Answer(question_id = answer['question_id'], user_id = current_user.user_id, value = answer['value'], date_created = datetime.now())
    db.session.merge(new_answer)
    db.session.commit()

    if question.type == 'select-multiple':
      answers = answer['value'].split(',')
      i = 1
      for cell in ws["A"]:
        if cell.internal_value == question.question_id:
          if str(i) in answers:
            ws.cell(row=cell.row, column=2).value = i
          i += 1
    else:
      for cell in ws["A"]:
        if cell.internal_value == question.question_id:
            ws.cell(row=cell.row, column=2).value = answer['value']

  wb.save(output_file)
    
  return jsonify("Vos réponses ont été sauvegardées!"), 200