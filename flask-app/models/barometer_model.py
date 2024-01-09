from database import db
from dataclasses import dataclass

@dataclass
class Barometer(db.Model):
    id: str
    section_id: str
    title: str
    about_barometer: str
    order: int 
    type: str
    min_result: float
    min_weight: float
    is_active: bool

    id = db.Column(db.String(20), primary_key = True)
    section_id = db.Column(db.String(20), db.ForeignKey( "section.id"))
    title = db.Column(db.String(255))
    about_barometer = db.Column(db.String(255))
    order = db.Column(db.Integer)
    type = db.Column(db.String(255))
    min_result = db.Column(db.Float)
    min_weight = db.Column(db.Float)
    is_active = db.Column(db.Boolean, default = True)