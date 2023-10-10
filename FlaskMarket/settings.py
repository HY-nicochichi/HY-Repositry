from datetime import timedelta
from orm import db

SECRET_KEY = 'Flask_Market_Secret_Key'
SESSION_COOKIE_HTTPONLY = True
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
SQLALCHEMY_DATABASE_URI = 'sqlite:///datastore.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SESSION_TYPE = 'sqlalchemy'
SESSION_SQLALCHEMY = db
