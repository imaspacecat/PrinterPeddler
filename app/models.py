from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    phone = db.Column(db.Integer)

class Printer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(1000))
    mx = db.Column(db.Integer)
    b = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    # materials =

    def to_json(self):
        return {
            "model": self.model,    
            "mx": self.mx,
            "b": self.b,
            "user_id": self.user_id
        }

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer = db.Column(db.Integer) # stores buyer id
    seller = db.Column(db.Integer) # stores seller id
    printer = db.Column(db.Integer) # stores printer id

    def to_json(self):
        return {
            "buyer": self.buyer,    
            "seller": self.seller,
            "printer": self.printer
        }




