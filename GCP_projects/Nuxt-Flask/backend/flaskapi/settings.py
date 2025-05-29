from os import getenv
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv('/.env')

SECRET_KEY = str(getenv('SECRET_KEY'))
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

SQLALCHEMY_DATABASE_URI = str(getenv('SQLALCHEMY_DATABASE_URI'))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

GOOGLE_CLIENT_ID = str(getenv('GOOGLE_CLIENT_ID'))
GOOGLE_CLIENT_SECRET = str(getenv('GOOGLE_CLIENT_SECRET'))

JWT_SECRET = str(getenv('JWT_SECRET'))
JWT_ALGORITHM = str(getenv('JWT_ALGORITHM'))
JWT_EXPIRES = timedelta(days=7)

CLIENT_DOMAINS = {
    'swagger_ui': 'http://localhost:5000',
    'web_front': 'http://localhost:8080'
}
