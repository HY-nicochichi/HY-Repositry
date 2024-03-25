from flask_sqlalchemy import SQLAlchemy
from .flask_beaker import BeakerSession
from flask_apscheduler import APScheduler
from flask_wtf.csrf import CSRFProtect
from .flask_talisman import Talisman
from datetime import datetime

db_orm = SQLAlchemy()
server_session = BeakerSession()
scheduler = APScheduler()
csrf_protect = CSRFProtect()
security_header = Talisman()

class BaseModel(db_orm.Model):

    __abstract__ = True

    id = db_orm.Column(db_orm.Integer, primary_key=True)
    created = db_orm.Column(db_orm.DateTime, default=datetime.now, nullable=False)
    updated = db_orm.Column(db_orm.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
