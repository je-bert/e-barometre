from flask_sqlalchemy import SQLAlchemy
from pandas import ExcelFile
from shutil import rmtree
from os import path
from sys import argv

DB_NAME = "database.db"
DB_ROOT_DIR = "instance"
DB_PATH = "{}/{}".format(DB_ROOT_DIR, DB_NAME)

db = SQLAlchemy()

def init(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  if not path.exists(DB_PATH) or (len(argv) > 1 and argv[1] == '--new'):
      run_seeds(app)
  else:
      db.init_app(app)

def run_seeds(app):
  if path.exists(DB_PATH):
    rmtree(DB_PATH.split('/')[0]) # Drop previous DB

  db.init_app(app) # Link new db

  xl = ExcelFile('seeds.xlsx')

  with app.app_context():

    db.create_all()  # Create tables
  
    for sheet_name in ['user']: #TODO (jeremie): Add seeds for other sheets (xl.sheet_names)
      sheet = xl.parse(sheet_name)
      sheet.to_sql(name=sheet_name, con=db.engine, if_exists='append', index=False)
      print("Created seeds for table", sheet_name)

