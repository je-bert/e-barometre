from database import db

class ResetPasswordToken(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    token = db.Column(db.String(255))
    date_created = db.Column(db.DateTime())

