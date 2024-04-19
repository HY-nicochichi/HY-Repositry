from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler
from flask_wtf.csrf import CSRFProtect
from .server_side_session import ServerSession
from .http_security_header import SecurityHeader
from datetime import datetime

db_orm = SQLAlchemy()
migration = Migrate()
server_session = ServerSession()
scheduler = APScheduler()
csrf_protect = CSRFProtect()
security_header = SecurityHeader()

class BaseModel(db_orm.Model):

    __abstract__ = True

    id = db_orm.Column(db_orm.Integer, primary_key=True)
    created = db_orm.Column(db_orm.DateTime, default=datetime.now, nullable=False)
    updated = db_orm.Column(db_orm.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
