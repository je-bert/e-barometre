from database import db

class Choice(db.Model):
    question_id = db.Column(db.String(20), primary_key = True)
    order = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.String(20))
    label = db.Column(db.String(100))