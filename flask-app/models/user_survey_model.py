from database import db
from dataclasses import dataclass

@dataclass
class UserSurvey(db.Model):
    user_survey_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    survey_id = db.Column(db.String(255), db.ForeignKey('survey.survey_id'))
    is_complete = db.Column(db.Boolean())
