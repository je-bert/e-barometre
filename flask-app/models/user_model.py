from database import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True)
    password = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    date_logged_in = db.Column(db.DateTime())
    date_created = db.Column(db.DateTime())
    role = db.Column(db.String(20))
