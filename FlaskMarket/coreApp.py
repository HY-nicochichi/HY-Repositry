from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from views1 import bp1
from views2 import bp2
from orm import db

app = Flask(__name__, static_folder='static')

app.config.from_pyfile('settings.py')

csrf_protect = CSRFProtect(app)

app.register_blueprint(bp1)
app.register_blueprint(bp2)

db.init_app(app)

server_side_session = Session(app)

with app.app_context():
    db.create_all()
