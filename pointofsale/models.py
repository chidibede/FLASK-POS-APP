'''
    Script that has all database models
    of the app. ORM (Object Relational Mapper)
     style models are used
'''
from pointofsale import db
from pointofsale import login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User Database Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(40), unique=True,  nullable=False)
    email = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    products = db.relationship('Product', backref='staff', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.fullname}', '{self.role}')"

class Product_Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return self.name

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500))
    qty_g = db.Column(db.Integer, default=0)
    qty_units = db.Column(db.Integer, default=0)
    cost_price = db.Column(db.Integer, nullable=False, default=0)
    selling_price = db.Column(db.Integer, nullable=False, default=0)
    category = db.Column(db.String(30), default='Grocery')
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

    def __repr__(self):
        return f"Product('{self.name}')"




