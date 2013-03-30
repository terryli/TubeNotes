import datetime

from database import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80))
    date = db.Column(db.DateTime)

    def __init__(self, key):
        self.key = key
        self.date = datetime.datetime.now()

    def __repr__(self):
        return '<Key %r>' % self.key


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return '<Name %r, Email %r>' % (self.name, self.email)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return '<Name %r, Email %r>' % (self.name, self.email)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    video = db.Column(db.Integer, db.ForeignKey('video.id'))
    text = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __init__(self, user, video, text):
        self.user = user
        self.video = video
        self.text = text.strip()
        self.date = datetime.datetime.now()

    def __repr__(self):
        return '<user %r, text %r>' % (self.user, self.text)
