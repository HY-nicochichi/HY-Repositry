from flask import Flask
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_migrate import Migrate
from views1 import bp1
from views2 import bp2
from orm import db

app = Flask(__name__)

app.config.from_pyfile('settings.py')

app.register_blueprint(bp1)
app.register_blueprint(bp2)

# security_header = Talisman(app)
csrf_protect = CSRFProtect(app)
server_side_session = Session(app)

db.init_app(app)

migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
