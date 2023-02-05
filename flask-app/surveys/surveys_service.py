from database import db
from surveys import Survey
from flask import render_template

def find_all():
  surveys = Survey.query.all()
  return render_template('surveys.html', surveys = surveys)