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

    # ============================= #
    # ======= Comment Calls ======= #

    def createComment(self, user, video, text):
        comment = Comment(user, video, text)
        db.session.add(comment)
        db.session.commit()
        return comment

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

    def countCommentsByVideo(self, vid):
        return Comment.query.filter_by(video=vid).count()

    def countCommentsByUser(self, uid):
        return Comment.query.filter_by(user=uid).count()

    def getCommentsByVideo(self, vid, limit=100, offset=0):
        return Comment.query.filter_by(video=vid).limit(limit).offset(offset).all()

    def getCommentsByUser(self, uid, limit=100, offset=0):
        return Comment.query.filter_by(user=uid).limit(limit).offset(offset).all()

    def getCommentById(self, cid):
        return Comment.query.filter_by(id=cid).first()

    # =========================== #
    # ======= Video Calls ======= #

    def createVideo(self, key):
        video = Video(key)
        db.session.add(video)
        db.session.commit()
        return video

    def getVideoByKey(self, key):
        return Video.query.filter_by(key=key).first()

    def getVideoById(self, vid):
        return Video.query.filter_by(id=vid).first()

    # ================== ======= #
    # ======= User Calls ======= #

    def createUser(self, name, password, email):
        user = User(name, password, email)
        db.session.add(user)
        db.session.commit()
        return user

    def deleteUser(self, uid):
        # delete comments
        user = User.query.filter_by(id=uid).first()
        db.session.delete(user)
        db.session.commit()
        return uid

    def getUserById(self, uid):
        return User.query.filter_by(id=uid).first()
