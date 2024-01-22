from database import db
from dataclasses import dataclass

@dataclass
class Indicator(db.Model):
    id: int
    barometer_id: str
    content: str
    id = db.Column(db.Integer, primary_key = True)
    barometer_id = db.Column(db.String(20), db.ForeignKey( "barometer.id", ondelete='CASCADE'), nullable = False)
    content = db.Column(db.String(100))
    items = db.relationship('BarometerItem', cascade="all,delete", backref='indicator')