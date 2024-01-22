from database import db
from dataclasses import dataclass

@dataclass
class BarometerActor(db.Model):
    id: int
    barometer_id: str
    actor_id: str
    id = db.Column(db.Integer, primary_key = True)
    barometer_id = db.Column(db.String(20), db.ForeignKey( "barometer.id", ondelete='CASCADE'), nullable = False)
    actor_id = db.Column(db.String(20), db.ForeignKey( "actor.id", ondelete='CASCADE'), nullable = False)
    behaviors = db.relationship('Behavior', cascade="all,delete", backref='barometer_actor')