from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext import uploads


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))
    name = db.Column(db.String(50))
    password = db.Column(db.String(255))
    email = db.Column(db.VARCHAR(320))

    def __init__(self,
                 username=username,
                 name=name,
                 password=password,
                 email=email):
        self.username = username
        self.name = name
        self.set_password(password)
        self.email = email

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password,
            method='pbkdf2:sha512:2000')

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def get_id(self):
        return self.id

    def __repr(self):
        return '<User %r>' % self.name


class Poop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128))
    #image = db.Column(db.Integer, db.ForeignKey('uploads.Upload.id'))