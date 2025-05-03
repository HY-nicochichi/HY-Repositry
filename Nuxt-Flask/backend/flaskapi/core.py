from flask import Flask
from views import bps
from extensions import (
    db_orm,
    jwt_manager,
    cross_origin
)

app = Flask(__name__)

app.config.from_pyfile('settings.py')

for bp in bps:
    app.register_blueprint(bp)

db_orm.init_app(app)
jwt_manager.init_app(app)
cross_origin.init_app(app)

with app.app_context():
    db_orm.create_all()
