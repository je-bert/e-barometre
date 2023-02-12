from database import db
from dataclasses import dataclass

@dataclass
class Label(db.Model):
    label_id: str
    order: int
    value: str
    label: str
    label_id = db.Column(db.String(20), primary_key = True)
    order = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.String(20))
    label = db.Column(db.String(100))

