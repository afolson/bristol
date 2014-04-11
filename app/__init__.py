from flask import Flask
from flask.ext import restful, uploads
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.restful import reqparse

login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object('config')
api = restful.Api(app)
db = SQLAlchemy(app)
# [todo] init uploads jawn

parser = reqparse.RequestParser()

login_manager.init_app(app)
login_manager.login_view = 'login'

from app import models, views, forms, jawn

api.add_resource(jawn.Registration, '/api/registration')
