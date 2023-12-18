from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_talisman import Talisman
from datetime import datetime
import pytz

db = SQLAlchemy()
migrate = Migrate()
csrf_protect = CSRFProtect()
server_side_session = Session()
security_header = Talisman()

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
