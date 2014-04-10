from app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))
    name = db.Column(db.String(50))
    email = db.Column(db.VARCHAR(320))

    def __init__(self,
                 username=username,
                 name=name,
                 email=email):
        self.username = username
        self.name = name
        self.email = email

    def __repr(self):
        return '<User %r>' % self.name
