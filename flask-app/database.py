from flask_sqlalchemy import SQLAlchemy
from pandas import ExcelFile
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
  if app_context != None:
    with app_context:
      xl = ExcelFile('seeds.xlsx')
      if path.exists(DB_PATH):
        db.drop_all() # Drop previous tables
      db.create_all()  # Create tables
      for sheet_name in ['user']: #TODO (jeremie): Add seeds for other sheets (xl.sheet_names)
        sheet = xl.parse(sheet_name)
        sheet.to_sql(name=sheet_name, con=db.engine, if_exists='append', index=False)
        print("Created seeds for table", sheet_name)

