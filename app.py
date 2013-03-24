import os
from flask import Flask
from flask import render_template
from flask import send_from_directory
from models import db

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://localhost/tubenotes')
app.config.update(
    DEBUG = True,
)

db.init_app(app)
with app.test_request_context():
    from models import Admin
    from models import Video
    db.create_all()

#----------------------------------------
# bootstrap
#----------------------------------------

admin_terry = Admin('Terry', 'tuber0')
admin_dorko = Admin('Dorko', 'tuber1')
with app.test_request_context():
    if (Admin.query.filter_by(name='Terry').first() is None):
        db.session.add(admin_terry)
    if (Admin.query.filter_by(name='Dorko').first() is None):
        db.session.add(admin_dorko)
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
    return render_template('index.html')

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
