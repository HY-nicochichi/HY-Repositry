from flask import Flask
from views import bps
from extensions import (
    db_orm,
    migration,
    server_session,
    scheduler,
    csrf_protect,
    security_header
)

app = Flask(__name__)

app.config.from_pyfile('settings.py')

for bp in bps:
    app.register_blueprint(bp)

db_orm.init_app(app)
migration.init_app(app, db_orm)
server_session.init_app(app)
scheduler.init_app(app)
csrf_protect.init_app(app)
security_header.init_app(app)

scheduler.start()
