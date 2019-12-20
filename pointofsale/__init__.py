''' 
Main App initialization Script (Pointofsale package)
Retail Point Of Sale.
Author: Chidi Bede Enwereji
Company: Emedia Bay
Client: Nelson Obiem
Client Company: 

'''

# Dependencies and Libraries needed
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# App Configurations and Database settings
app = Flask("__name__", template_folder='pointofsale/templates', static_folder='pointofsale/static')
app.config['SECRET_KEY'] = '9afddcaac4139568d4d46a6bd0f8127f'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posdatabase.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Views
from pointofsale import views