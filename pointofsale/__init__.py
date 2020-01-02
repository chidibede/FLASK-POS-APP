''' 
Main App initialization Script (Pointofsale package)
Retail Point Of Sale.
Author: Chidi Bede Enwereji
Company: Emedia Bay
Client: Nelson Obiem
Client Company: 

'''

# Dependencies and Libraries needed
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class



# App Configurations and Database settings
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask("__name__", template_folder='pointofsale/templates', static_folder='pointofsale/static')
app.config['SECRET_KEY'] = '9afddcaac4139568d4d46a6bd0f8127f'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posdatabase.db"

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/img')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



# Views
from pointofsale import views
