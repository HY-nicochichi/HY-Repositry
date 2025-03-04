from datetime import timedelta
from flask import Flask
from views import bps
from extensions import (
    db_orm,
    jwt_manager,
    cross_origin
)

app = Flask('test')

app.config.from_pyfile('/flaskapi/settings.py')
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////flaskapi/test.db'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=10)

for bp in bps:
    app.register_blueprint(bp)

db_orm.init_app(app)
jwt_manager.init_app(app)
cross_origin.init_app(app)

with app.app_context():
    db_orm.create_all()
