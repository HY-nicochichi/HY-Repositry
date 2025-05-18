from datetime import datetime
from werkzeug.local import LocalProxy
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from .oauth_jwt import OAuthJWT

db_orm = SQLAlchemy()
auth_manager = OAuthJWT()
cross_origin = CORS()

class TableBase(db_orm.Model):
    __abstract__ = True
    id : Mapped[str] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)
    updated: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now, nullable=False)

user_info = LocalProxy(lambda: auth_manager.user_info())
