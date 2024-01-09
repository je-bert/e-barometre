from database import db
from dataclasses import dataclass

@dataclass
class Theme(db.Model):
  id: str
  barometer_id: str
  name: str
  is_active: bool
  
  id = db.Column(db.String(20), primary_key = True)
  barometer_id = db.Column(db.String(20), db.ForeignKey( "barometer.id"))
  name = db.Column(db.String(255))
  is_active = db.Column(db.Boolean, default = True)