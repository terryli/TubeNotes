from database import db

import string
import urlparse

from models import Admin
from models import Comment
from models import User
from models import Video

class Handler():

    def __init__(self):
        pass

    def getAdmins(self):
        return Admin.query.all()

    def getKey(self, url):
        if string.find(url, 'youtube.com') > 0:
            parsed = urlparse.urlparse(url)
            return urlparse.parse_qs(parsed.query).get('v').pop()
        else:
            return url

    def countCommentsByVideo(self, video):
        return Comment.query.filter_by(video=video).count()

    def countCommentsByUser(self, user):
        return Comment.query.filter_by(user=user).count()

    def getCommentsByVideo(self, video):
        # add starting index and row count
        return Comment.query.filter_by(video=video)

    def getCommentsByUser(self, user):
        # add starting index and row count
        return Comment.query.filter_by(user=user)

    def getVideoByKey(self, key):
        return Video.query.filter_by(key=key).first()

    def getVideoById(self, vid):
        return Video.query.filter_by(id=vid).first()

    def createVideo(self, key):
        video = Video(key)
        db.session.add(video)
        db.session.commit()
        return video.id

    def createComment(self, user, video, text):
        comment = Comment(user, video, text)
        db.session.add(comment)
        db.session.commit()
        return comment.id

    def deleteComment(self, cid):
        comment = Comment.query.filter_by(id=cid).first()
        db.session.delete(comment)
        db.session.commit()
        return cid

    def editComment(self, cid, text):
        comment = Comment.query.filter_by(id=cid).first()
        comment.text = text
        db.session.commit()
        return cid

    def createUser(self, name, password, email):
        user = User(name, password, email)
        db.session.add(user)
        db.session.commit()
        return user.id

    def deleteUser(self, uid):
        user = User.query.filter_by(id=uid).first()
        db.session.delete(user)
        db.session.commit()
        return uid
