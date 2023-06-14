from flask import abort, jsonify, render_template
from models import User, Answer, Question
import os
from database import db
from shutil import copyfile
import os
from openpyxl import load_workbook
from pycel import ExcelCompiler

def generate():
  convert_xlookup_to_index_match()
  user_id = 1

  user = User.query\
    .filter_by(user_id = user_id)\
    .first()

  if not user:
      return abort(400)
  
  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  template_file = 'Master_TEST_Barometre_230523_8h00_3.xlsx'
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

  return jsonify("Votre rapport a été généré!"), 200

def output():
  user_id = 1

  user = User.query\
    .filter_by(user_id = user_id)\
    .first()

  if not user:
      return abort(400)

  if not os.path.exists('master_results'):
    os.makedirs('master_results')

  filename = 'master_results/{}.xlsx'.format(user_id)

  if not os.path.exists(filename):
     return abort(404)
  
  worksheet_name = 'Test de contenu du rapport'

  excel = ExcelCompiler(filename=filename)

  results = []

  for i in range(1,450):
    cell = excel.evaluate(f"'{worksheet_name}'!B{i}")
    if cell:
       results.append(cell)

  return render_template('results-test.html', user = user, results = results)

def convert_xlookup_to_index_match():
  filename = 'Master_TEST_Barometre_230523_8h00_3.xlsx'
  sheetname = 'Modèle Calcul A-R + Sommaire'
  cell_range = 'D32:U800'

  # Load the workbook
  workbook = load_workbook(filename)
  worksheet = workbook[sheetname]

  # Get the cell range
  cells = worksheet[cell_range]

  for row in cells:
      for cell in row:
          # Get the formula from the cell
          formula = cell.value
          print(formula)
          # Check if the formula is an XLOOKUP formula
          if formula and not isinstance(formula, int) and  formula.startswith('=_xlfn.XLOOKUP('):
              lookup_args = formula[15:-1].split(',')
              search_value = lookup_args[0].strip()
              lookup_range = lookup_args[1].strip()
              return_range = lookup_args[2].strip()

              # Replace the XLOOKUP formula with INDEX and MATCH formula
              index_match_formula = f'=_xlfn.INDEX({return_range}, _xlfn.MATCH({search_value}, {lookup_range}, 0), 1)'
              cell.value = index_match_formula

  # Save the updated workbook
  workbook.save(filename)
  return "Success",200
