from flask import Flask
from flask.ext import uploads, restless
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
# [todo] init uploads jawn

manager = restless.APIManager(app, flask_sqlalchemy_db=db)

login_manager.init_app(app)
login_manager.login_view = 'login'

from app import models, forms, jawn
