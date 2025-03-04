from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)

class ModelClass(DeclarativeBase):
    pass

db_orm = SQLAlchemy(model_class=ModelClass)
jwt_manager = JWTManager()
cross_origin = CORS()

class TableBase(db_orm.Model):
    __abstract__ = True
    id : Mapped[str] = mapped_column(nullable=False, primary_key=True)
    created: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)
    updated: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now, nullable=False)
