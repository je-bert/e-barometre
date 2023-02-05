from database import db

class Category(db.Model):
  category_id = db.Column(db.String(255), primary_key = True)
  label = db.Column(db.String(255))