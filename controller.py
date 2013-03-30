from handler import Handler

from flask import render_template

from models import Admin
from models import Comment
from models import User
from models import Video

class Controller():

    def __init__(self):
        pass

    def testCalls(self, url):
        handler = Handler()
        if url:
            key = handler.getKey(url)
            print "----"
            print url
            print key
            print "===="

    def signUp(self):
        pass

    def signIn(self):
        pass

    def signOut(self):
        pass

    def run(self):
        admins = Admin.query.all()
        return render_template('index.html', admins=admins)
