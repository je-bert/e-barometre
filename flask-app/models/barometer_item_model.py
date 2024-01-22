from database import db
from dataclasses import dataclass

@dataclass
class BarometerItem(db.Model):
  id: str
  barometer_id: str
  theme_id: int 
  behavior_id: int
  actor_id: int
  indicator_id: int
  content: str
  min: float
  max: float
  type: str
  is_active: bool
  is_unavoidable: bool
  condition: str

  id = db.Column(db.String(20), primary_key = True)
  barometer_id = db.Column(db.String(20), db.ForeignKey( "barometer.id", ondelete='CASCADE'), nullable = False)
  theme_id = db.Column(db.Integer, db.ForeignKey( "theme.id", ondelete='CASCADE'), nullable = True)
  behavior_id = db.Column(db.Integer, db.ForeignKey( "behavior.id", ondelete='CASCADE'), nullable = True)
  actor_id = db.Column(db.Integer, db.ForeignKey( "barometer_actor.id", ondelete='CASCADE'), nullable = True)
  indicator_id = db.Column(db.Integer, db.ForeignKey( "indicator.id", ondelete='CASCADE'), nullable = True)
  content = db.Column(db.String(255))
  min = db.Column(db.Float(20))
  max = db.Column(db.Float(20))
  type = db.Column(db.String(20))
  is_active = db.Column(db.Boolean, default = True)
  is_unavoidable = db.Column(db.Boolean, default = False)
  condition = db.Column(db.String(255), nullable = True, default = None)