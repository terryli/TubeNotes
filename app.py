import os

from flask import Flask
from flask import render_template
from flask import send_from_directory

from models import db
from models import Admin
from models import Video

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

#----------------------------------------
# bootstrap
#----------------------------------------

if (Admin.query.filter_by(name='Terry').first() is None):
    db.session.add(Admin('Terry', 'tuber0'))
if (Admin.query.filter_by(name='Dorko').first() is None):
    db.session.add( Admin('Dorko', 'tuber1'))
db.session.commit()

#----------------------------------------
# controllers
#----------------------------------------

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    admins = Admin.query.all()
    return render_template('index.html', admins=admins)

@app.route("/show")
def show():
    admins = Admin.query.all()
    return render_template('show.html', admins=admins)

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
