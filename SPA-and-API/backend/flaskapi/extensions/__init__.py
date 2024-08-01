from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .http_security_header import SecurityHeader
from flask_cors import CORS
from datetime import datetime, timezone

db_orm = SQLAlchemy()
jwt_manager = JWTManager()
security_header = SecurityHeader()

cors_jwt = CORS()
cors_user = CORS()

class BaseModel(db_orm.Model):

    __abstract__ = True

    id = db_orm.Column(db_orm.Integer, primary_key=True)
    created = db_orm.Column(db_orm.DateTime, default=lambda:datetime.now(timezone.utc), nullable=False)
    updated = db_orm.Column(db_orm.DateTime, default=lambda:datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc), nullable=False)
