from database import db

class CustomAnswer(db.Model):
    question_id = db.Column(db.String(20), primary_key = True)
    report_id = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.String(255))
    date_created = db.Column(db.DateTime())