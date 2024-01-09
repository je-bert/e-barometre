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
    min_result_note: str
    min_weight: float
    min_weight_note: str
    is_active: bool

    id = db.Column(db.String(20), primary_key = True)
    section_id = db.Column(db.String(20), db.ForeignKey( "section.id"))
    title = db.Column(db.String(255))
    about_barometer = db.Column(db.String(255))
    order = db.Column(db.Integer)
    type = db.Column(db.String(255))
    min_result = db.Column(db.Float)
    min_result_note = db.Column(db.String(255))
    min_weight = db.Column(db.Float)
    min_weight_note = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default = True)