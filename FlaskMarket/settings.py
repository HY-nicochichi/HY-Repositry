from datetime import timedelta
from orm import db

SECRET_KEY = 'Flask_Market_Secret_Key'
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
SESSION_TYPE = 'sqlalchemy'
SESSION_SQLALCHEMY = db
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False
TESTING = True
