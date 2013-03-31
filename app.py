import os

from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
from flask.ext.bcrypt import Bcrypt

from controller import Controller
from database import db
from models import Admin

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://localhost/tubenotes')
app.config.update(
    DEBUG = True,
)

db.init_app(app)
db.app = app
db.create_all()

bcrypt = Bcrypt(app)

#----------------------------------------
# bootstrap
#----------------------------------------

if (Admin.query.filter_by(name='Terry').first() is None):
    db.session.add(Admin('Terry', 'tuber0', 'terry@tuber.com'))
if (Admin.query.filter_by(name='Dorko').first() is None):
    db.session.add( Admin('Dorko', 'tuber1', 'dorko@tuber.com'))
db.session.commit()

#----------------------------------------
# controllers
#----------------------------------------

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    url = request.args.get('url')
    # this should create or pull the right video id, then render
    # show.html with the right video id
    controller = Controller()
    controller.testCalls(url)
    return controller.run()

@app.route("/signup")
def signup():
    #pw_hash = bcrypt.generate_password_hash('hunter2')
    return render_template('signup.html')

@app.route("/video/<int:param>")
def show(param):
    print param
    print "===="
    admins = Admin.query.all()
    print admins
    return render_template('show.html', admins=admins)

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
