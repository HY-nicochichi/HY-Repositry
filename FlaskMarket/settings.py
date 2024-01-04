from datetime import timedelta
from extensions import db_orm

SECRET_KEY = 'Flask_Market_Secret_Key'
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
SESSION_TYPE = 'sqlalchemy'
SESSION_SQLALCHEMY = db_orm
SESSION_COOKIE_SAMESITE = 'Lax'
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False
TESTING = True
