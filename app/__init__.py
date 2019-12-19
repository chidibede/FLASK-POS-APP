''' Dependencies and Libraries needed '''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


''' App Configurations and Database settings '''
app = Flask("__name__", template_folder='app/templates', static_folder='app/static')
app.config['SECRET_KEY'] = '9afddcaac4139568d4d46a6bd0f8127f'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posdatabase.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from app import views