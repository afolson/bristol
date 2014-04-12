from flask import Flask
from flask.ext import uploads
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
# [todo] init uploads jawn

login_manager.init_app(app)
login_manager.login_view = 'login'

from app import models, views, forms, jawn
