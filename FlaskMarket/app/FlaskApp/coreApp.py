from flask import Flask
from views1 import bp1
from views2 import bp2
from orm import db

app = Flask(__name__)

app.config.from_pyfile('settings.py')

app.register_blueprint(bp1)
app.register_blueprint(bp2)

db.init_app(app)

with app.app_context():
    db.create_all()
