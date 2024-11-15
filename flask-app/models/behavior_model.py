from database import db
from dataclasses import dataclass

@dataclass
class Behavior(db.Model):
  id: str
  theme_id: str
  question_id: str
  ranges: str
  weight: float
  is_active: bool
  actor_id: int

  id = db.Column(db.String(20), primary_key = True)
  theme_id = db.Column(db.String(20), db.ForeignKey( "theme.id", ondelete='CASCADE'))
  question_id = db.Column(db.String(20), db.ForeignKey( "question.question_id", ondelete='CASCADE'))
  actor_id = db.Column(db.Integer, db.ForeignKey( "barometer_actor.id", ondelete='CASCADE'), nullable = True)
  items = db.relationship('BarometerItem', cascade="all,delete", backref='behavior')
  ranges = db.Column(db.String(100))
  weight = db.Column(db.Float)
  is_active = db.Column(db.Boolean, default = True)
