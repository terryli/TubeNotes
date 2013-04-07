import datetime

from database import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80))
    date = db.Column(db.DateTime)
    # active = db.Column(db.Boolean)

    def __init__(self, key):
        self.key = key
        self.date = datetime.datetime.now()
        # self.active = True

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
    # active = db.Column(db.Boolean)

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
        # self.active = True

    def __repr__(self):
        return '<Name %r, Email %r>' % (self.name, self.email)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    video = db.Column(db.Integer, db.ForeignKey('video.id'))
    text = db.Column(db.Text)
    time = db.Column(db.Float)
    date = db.Column(db.DateTime)
    # active = db.Column(db.Boolean)

    def __init__(self, user, video, text, time):
        self.user = user
        self.video = video
        self.text = text.strip()
        self.time = time
        self.date = datetime.datetime.now()
        # self.active = True

    def __repr__(self):
        return '<time %r, user %r, text %r>' % (self.time, self.user, self.text)
