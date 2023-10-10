from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

db = SQLAlchemy()

class BaseModel(db.Model):

    __abstract__ = True

    created_at = db.Column(
        db.DateTime(timezone=True),
        default = lambda:datetime.now(pytz.timezone('Asia/Tokyo')),
        nullable = False)
    
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default = lambda:datetime.now(pytz.timezone('Asia/Tokyo')),
        onupdate = lambda:datetime.now(pytz.timezone('Asia/Tokyo')),
        nullable = False)
