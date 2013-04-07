from handler import Handler

from flask import redirect, render_template

class Controller():

    def __init__(self):
        self.handler = Handler()

    def findVideo(self, url):
        key = self.handler.getKey(url)
        video = self.handler.getVideoByKey(key)
        if (video is None):
            video = self.handler.createVideo(key)
        return redirect("/video/" + str(video.id))

    def showVideo(self, vid, offset=0):
        video = self.handler.getVideoById(vid)
        if (video is not None):
            total = self.handler.countCommentsByVideo(vid)
            comments = self.handler.getCommentsByVideo(vid, 100, offset)
            return render_template('show.html', 
                                   key=video.key, 
                                   total=total,
                                   comments=comments)
        else:
            return render_template('404.html')

    def showComment(self, cid):
        comment = self.handler.getCommentById(cid)
        if (comment is not None):
            return return_template('comment.html', comment=comment)
        else:
            return render_template('404.html')

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
