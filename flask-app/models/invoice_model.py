from database import db

class Invoice(db.Model):
    invoice_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey( "user.user_id"))
    amount_subtotal = db.Column(db.Integer)
    amount_tax = db.Column(db.Integer)
    amount_discount = db.Column(db.Integer)
    amount_total = db.Column(db.Integer)
    price_id = db.Column(db.String(30))
    status = db.Column(db.String(20))
    date_expiration = db.Column(db.DateTime())
    date_created = db.Column(db.DateTime())
    session_id = db.Column(db.String(100))