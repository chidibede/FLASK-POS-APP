'''
    Script that has all database models
    of the app. ORM (Object Relational Mapper)
     style models are used
'''
from pointofsale import db

# User Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(40), unique=True,  nullable=False)
    email = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(60), nullable=False)


    def __repr__(self):
        return f"User('{self.username}', '{self.fullname}', '{self.role}')"
