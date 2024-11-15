from database import db
from dataclasses import dataclass

@dataclass
class Answer(db.Model):
    question_id: str
    report_id: int
    value: str
    question_id = db.Column(db.String(20), primary_key = True)
    report_id = db.Column(db.Integer, db.ForeignKey( "report.report_id"), primary_key = True)
    value = db.Column(db.String(255))
    date_created = db.Column(db.DateTime())