from handler import Handler

from flask import render_template

class Controller():

    def __init__(self):
        self.handler = Handler()

    def testCalls(self, url):
        if url:
            key = self.handler.getKey(url)
            print key

    def findVideo(self, url):
        key = self.handler.getKey(url)
        video = self.handler.getVideoByKey(key)
        if (video is None):
            self.handler.createVideo(key)
        return render_template('show.html', key=key)

    def showVideo(self, vid):
        video = self.handler.getVideoById(vid)
        if (video is not None):
            return render_template('show.html', key=video.key)
        else:
            return render_template('404.html')

    def showComment(self, cid):
        pass

    def signUp(self):
        pass

    def signIn(self):
        pass

    def signOut(self):
        pass

    def run(self):
        # render basic index with input box for youtube link or key
        # should dynamically check at JS level if key is legit
        # if so, call self with url parameter to be handled
        admins = self.handler.getAdmins()
        return render_template('index.html', admins=admins)
