from datetime import timedelta

SECRET_KEY = 'Secret_Key'
SESSION_COOKIE_HTTPONLY = True
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
SQLALCHEMY_DATABASE_URI = 'sqlite:///datastore.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
