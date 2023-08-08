from database import db
from dataclasses import dataclass

@dataclass
class Label(db.Model):
    label_id: str
    label_id = db.Column(db.String(20), primary_key = True)
