from flask_sqlalchemy import SQLAlchemy
from pandas import ExcelFile, set_option
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

def run_seeds(file_name = 'seeds.xlsx'):
  # importing models is required for ORM
  from models import Survey, Category, User, Choice, Question, Label, LabelItem, Answer, CustomAnswer, ResetPasswordToken, AnalysisSection, AnalysisSubsection, Invoice
  if app_context != None:
    with app_context:
      xl = ExcelFile(file_name)
      db.reflect()
      db.drop_all() # Drop previous tables
      db.create_all()  # Create tables
      for model in [Survey, Category, User, Choice, Question, Label, LabelItem, Answer, CustomAnswer, AnalysisSection, AnalysisSubsection, Invoice]:
        if model.__tablename__ in xl.sheet_names:
          sheet = xl.parse(model.__tablename__)
          sheet.to_sql(name=model.__tablename__, con=db.engine, if_exists='append', index=False)
          print(" * DB: Created seeds for table", model.__tablename__)

