from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_talisman import Talisman
from flask_cors import CORS
from datetime import datetime

db_orm = SQLAlchemy()
jwt_manager = JWTManager()
security_header = Talisman()

cors_jwt = CORS()
cors_user = CORS()

class BaseModel(db_orm.Model):

    __abstract__ = True

    id = db_orm.Column(db_orm.Integer, primary_key=True)
    created = db_orm.Column(db_orm.DateTime, default=datetime.now, nullable=False)
    updated = db_orm.Column(db_orm.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
