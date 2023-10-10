from database import db
from dataclasses import dataclass

@dataclass
class Choice(db.Model):
    question_id: str
    order: int
    value: str
    label: str
    intensity: int
    question_id = db.Column(db.String(20), primary_key = True)
    value = db.Column(db.String(255), primary_key = True)
    order = db.Column(db.Integer) 
    label = db.Column(db.String(255))
    intensity = db.Column(db.Integer)