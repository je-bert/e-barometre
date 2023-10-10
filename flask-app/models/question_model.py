from database import db
from dataclasses import dataclass

@dataclass
class Question(db.Model):
  question_id: str
  survey_id: str
  intro: str
  title: str
  type: str
  label_id: str
  info_bubble_text: str
  condition: str
  intensity: int
  conditional_intensity: str
  order: int
  parent: str
  intensity_method: str
  question_id = db.Column(db.String(20), primary_key = True)
  survey_id = db.Column(db.String(20), db.ForeignKey( "survey.survey_id"))
  intro = db.Column(db.String(255), nullable = True)
  title = db.Column(db.String(255))
  type = db.Column(db.String(20))
  label_id = db.Column(db.String(20), nullable = True)
  info_bubble_text = db.Column(db.String(1000), nullable = True)
  condition = db.Column(db.String(255), nullable = True)
  intensity = db.Column(db.Integer, nullable = True)
  conditional_intensity = db.Column(db.String(255), nullable = True)
  order = db.Column(db.Integer)
  min_value = db.Column(db.Integer, nullable = True)
  max_value = db.Column(db.Integer, nullable = True)
  active = db.Column(db.Integer, nullable = True)
  violence_related = db.Column(db.Integer, nullable = True)
  parent = db.Column(db.String(20), nullable = True)
  ladderC	= db.Column(db.Integer, nullable = True)
  ladderE	= db.Column(db.Integer, nullable = True)
  ladderV = db.Column(db.Integer, nullable = True)	
  red_flag = db.Column(db.Integer, nullable = True)
  past_intro	= db.Column(db.String(255), nullable = True)
  past_title = db.Column(db.String(255), nullable = True)
  intensity_method = db.Column(db.String(255), nullable = True)