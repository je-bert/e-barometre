from database import db
from dataclasses import dataclass

@dataclass
class Label(db.Model):
    label_id: str
    title: str
    label_id = db.Column(db.String(20), primary_key = True)
    title = db.Column(db.String(255))

