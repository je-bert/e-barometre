from database import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Report(db.Model):
    report_id: int
    user_id: int
    name: str
    date_created: datetime
    is_completed: bool

    report_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey( "user.user_id"))
    name = db.Column(db.String(30))
    date_created = db.Column(db.DateTime())
    is_completed = db.Column(db.Boolean, default = False)