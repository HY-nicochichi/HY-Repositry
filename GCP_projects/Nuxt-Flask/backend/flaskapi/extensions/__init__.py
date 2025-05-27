from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from .auth_manage_ext import AuthManager

db_orm = SQLAlchemy()
auth_manager = AuthManager()
cross_origin = CORS(supports_credentials=True)

class TableBase(db_orm.Model):
    __abstract__ = True
    id : Mapped[str] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)
    updated: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now, nullable=False)
