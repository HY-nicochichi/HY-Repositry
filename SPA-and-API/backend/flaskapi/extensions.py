from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

db_orm = SQLAlchemy()
jwt_manager = JWTManager()
cross_origin = CORS()

class TableBase(db_orm.Model):
    __abstract__ = True
    id : Mapped[str] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(default=lambda:datetime.now(), nullable=False)
    updated: Mapped[datetime] = mapped_column(default=lambda:datetime.now(), onupdate=lambda:datetime.now(), nullable=False)
