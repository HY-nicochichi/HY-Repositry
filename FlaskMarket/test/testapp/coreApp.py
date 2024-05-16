from flask import Flask
from views import bps
from extensions import db_orm

def create_app():

    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    for bp in bps:
        app.register_blueprint(bp)

    db_orm.init_app(app)
    
    return app
