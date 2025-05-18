from os import getenv
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv('/.env')

SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7.0)
