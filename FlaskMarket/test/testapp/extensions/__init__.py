from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db_orm = SQLAlchemy()

class BaseModel(db_orm.Model):

    __abstract__ = True

    id = db_orm.Column(db_orm.Integer, primary_key=True)
    created = db_orm.Column(db_orm.DateTime, default=datetime.now, nullable=False)
    updated = db_orm.Column(db_orm.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
