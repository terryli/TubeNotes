from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80))

    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return '<Key %r>' % self.key
