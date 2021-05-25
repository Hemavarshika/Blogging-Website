from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY']='f0e65964053572477ac475438be65234'
# to prevent cookies
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db= SQLAlchemy(app)
bcrypt=Bcrypt(app)
# for unique password
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from flaskblog import routes
