from database import db
from dataclasses import dataclass

@dataclass
class Actor(db.Model):
    id: str
    name: str
    id = db.Column(db.String(20), primary_key = True)
    name = db.Column(db.String(100))
    barometer_actors = db.relationship('BarometerActor', cascade="all,delete", backref='actor')