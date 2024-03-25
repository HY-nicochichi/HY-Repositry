from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from extensions.flask_beaker import BeakerSession
from flask_apscheduler import APScheduler
from flask_wtf.csrf import CSRFProtect
from extensions.flask_talisman import Talisman
from datetime import datetime

db_orm = SQLAlchemy()
migration = Migrate()
server_session = BeakerSession()
scheduler = APScheduler()
csrf_protect = CSRFProtect()
security_header = Talisman()

class BaseModel(db_orm.Model):

    __abstract__ = True

    id = db_orm.Column(db_orm.Integer, primary_key=True)
    created_at = db_orm.Column(db_orm.DateTime, default=lambda:datetime.now(), nullable=False)
    updated_at = db_orm.Column(db_orm.DateTime, default=lambda:datetime.now(), onupdate=lambda:datetime.now(), nullable=False)
