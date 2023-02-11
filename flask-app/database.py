from flask_sqlalchemy import SQLAlchemy
from pandas import ExcelFile, options
from os import path
from sys import argv

DB_NAME = "database.db"
DB_ROOT_DIR = "instance"
DB_PATH = "{}/{}".format(DB_ROOT_DIR, DB_NAME)

db = SQLAlchemy()
app_context = None

def init(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)
  global app_context
  app_context = app.app_context()
  if not path.exists(DB_PATH) or (len(argv) > 1 and argv[1] == '--new'):
      run_seeds()

def run_seeds():
  # importing models is required for ORM
  from surveys import Survey
  from categories import Category
  from users import User
  from choices import Choice
  from questions import Question
  from labels import Label
  if app_context != None:
    with app_context:
      xl = ExcelFile('seeds.xlsx')
      db.reflect()
      db.drop_all() # Drop previous tables
      db.create_all()  # Create tables
      for sheet_name in xl.sheet_names:
        sheet = xl.parse(sheet_name)
        sheet.to_sql(name=sheet_name, con=db.engine, if_exists='append', index=False)
        print(" * DB: Created seeds for table", sheet_name)

