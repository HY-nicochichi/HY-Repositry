from flask import Flask
from views1 import bp1
from views2 import bp2
from extensions import (
    db_orm, 
    migration,
    server_session,
    csrf_protect, 
    security_header
)

app = Flask(__name__)

app.config.from_pyfile('settings.py')

app.register_blueprint(bp1)
app.register_blueprint(bp2)

db_orm.init_app(app)
migration.init_app(app, db_orm)
server_session.init_app(app)
csrf_protect.init_app(app)
# security_header.init_app(app)

with app.app_context():
    db_orm.create_all()
