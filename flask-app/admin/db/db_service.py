from flask import render_template, send_file, after_this_request, session, request, redirect, url_for
from models import Survey, Category, User, Choice, Question, Label, Answer, CustomAnswer
import pandas as pd
from database import db, run_seeds
import os
from datetime import datetime

def get_view():
  return render_template('db.html')

def export_db():
  now = datetime.now()
  file_name = now.strftime('e_barometre_db_%Y_%m_%d_%H%M%S.xlsx')
  with db.engine.connect() as conn:
    with pd.ExcelWriter(file_name) as writer:
          writer.book.create_sheet("info")
          df_info = pd.DataFrame([[now.strftime('%Y-%m-%d %H:%M:%S')], [session['email']]], index=['Généré le :', 'Par :'])
          df_info.to_excel(writer, sheet_name='info', header=False)
          for model in [Survey, Category, User, Choice, Question, Label, Answer, CustomAnswer]:
              df = pd.read_sql_table(model.__tablename__, conn)
              df.to_excel(writer, sheet_name=model.__tablename__, index=False)
    @after_this_request
    def remove_file(response):
        os.remove(os.getcwd() + '/' + file_name)
        return response
    return send_file(file_name, as_attachment=True)

def import_db():
  file = request.files['file']
  now = datetime.now()
  file_name = now.strftime('e_barometre_db_%Y_%m_%d_%H%M%S.xlsx')
  file.save(file_name)
  @after_this_request
  def remove_file(response):
      os.remove(os.getcwd() + '/' + file_name)
      return response
  run_seeds(file_name)
  return redirect(url_for("admin_router.surveys_router.find_all"))

def reset_db():
  run_seeds()
  return redirect(url_for("admin_router.surveys_router.find_all"))