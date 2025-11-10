from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    is_admin = db.Column(db.Boolean, default=False)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.Float)
    location = db.Column(db.String(120))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(200))
    is_sold = db.Column(db.Boolean, default=False)
