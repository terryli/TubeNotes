from database import db

from models import Video

class Handler():

    def __init__(self, key):
        self.key = key

    def getComments(self):
        return "HAHA"

    def getVideoInfo(self):
        return Video.query.filter_by(key=self.key).first()
