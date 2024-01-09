from database import db
from dataclasses import dataclass

@dataclass
class Section(db.Model):
    id: str
    title: str
    order: int 
    is_active: bool

    id = db.Column(db.String(20), primary_key = True)
    title = db.Column(db.String(255))
    order = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default = True)