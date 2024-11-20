from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)

class BaseModel(DeclarativeBase):
    pass

db_orm = SQLAlchemy(model_class=BaseModel)
jwt_manager = JWTManager()
cross_origin = CORS()

class TimeStampModel(db_orm.Model):

    __abstract__ = True

    created_time: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)
    updated_time: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now, nullable=False)
