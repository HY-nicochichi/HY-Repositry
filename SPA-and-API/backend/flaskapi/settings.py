from datetime import timedelta

# utf-8
JSON_AS_ASCII = False

# db_orm
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@database:5432/postgres'
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# jwt_manager
JWT_SECRET_KEY = 'jwt_secret_key'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7.0)
