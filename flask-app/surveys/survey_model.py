from database import db
from sqlalchemy.orm import column_property
from sqlalchemy import select, func
from questions import Question

class Survey(db.Model):
    survey_id = db.Column(db.String(20), primary_key = True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    color = db.Column(db.String(20))
    cover_picture_url = db.Column(db.String(255))
    status = db.Column(db.String(20))
    order = db.Column(db.Integer)
    questions_count = column_property(
        select(func.count(Question.question_id))
        .where(Question.survey_id == survey_id)
        .scalar_subquery()
    )

