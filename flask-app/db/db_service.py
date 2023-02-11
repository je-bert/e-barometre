from flask import render_template, send_file, after_this_request
from surveys import Survey
from categories import Category
from users import User
from choices import Choice
from questions import Question
from labels import Label
import pandas as pd
from database import db
import os
from datetime import datetime

def get():
  return render_template('db.html')

def export():
  file_name = datetime.now().strftime('e_barometre_db_%Y_%m_%d_%H%M%S.xlsx')
  with db.engine.connect() as conn:
    with pd.ExcelWriter(file_name) as writer:
          writer.book.create_sheet("info")
          for model in [Survey, Category, User, Choice, Question, Label]:
              df = pd.read_sql_table(model.__tablename__, conn)
              df.to_excel(writer, sheet_name=model.__tablename__, index=False)
    @after_this_request
    def remove_file(response):
        os.remove(os.getcwd() + '/' + file_name)
        return response
    return send_file(file_name, as_attachment=True)