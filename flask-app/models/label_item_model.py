from database import db
from dataclasses import dataclass

@dataclass
class LabelItem(db.Model):
    label_item_id: str
    label_id: str
    order: int
    value: int
    label: str
    label_item_id = db.Column(db.String(20), primary_key = True)
    label_id = db.Column(db.String(20), db.ForeignKey( "label.label_id"))
    order = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.Integer)
    label = db.Column(db.String(100))