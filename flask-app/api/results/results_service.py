from flask import render_template, send_file, abort
from models import User, Answer, Question
import os
from database import db
from shutil import copyfile
import os
from openpyxl import load_workbook

def generate(current_user):
  user_id = current_user.user_id

  user = User.query\
    .filter_by(user_id = user_id)\
    .first()

  if not user:
      return abort(400)
  
  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  template_file = 'master_test_2.xlsx'
  worksheet_name = 'TEST_pour PROTOTYPE'
  output_file = 'master_results/{}.xlsx'.format(user.user_id)
  if not os.path.exists(output_file):
     copyfile(template_file, output_file)

  # Load the workbook and access the sheet we'll paste into
  wb = load_workbook(output_file)
  ws = wb.get_sheet_by_name(worksheet_name)

  answers = Answer.query\
    .filter_by(user_id = user_id)\
    .all()

  for answer in answers:
    question = Question.query\
          .filter_by(question_id = answer.question_id )\
          .first()
    if question.type == 'select-multiple':
      values = answer.value.split(',')
      i = 1
      for cell in ws["C"]:
        if type(cell).__name__ != 'MergedCell' and cell.internal_value == answer.question_id:
          ws.cell(row=cell.row, column=4).value = 1 if str(i) in values else 0
          i += 1
    else:
      for cell in ws["C"]:
        if type(cell).__name__ != 'MergedCell' and cell.internal_value == answer.question_id:
            ws.cell(row=cell.row, column=4).value = answer.value
  
  wb.save(output_file)

  return render_template('results.html', results = [])