from datetime import timedelta

# 以下の２項目は本番ではAWSのSecretManager等で厳重保管すべし
secret_key = 'Flask_Market_Secret_Key'
database_url = 'sqlite:///test.db'

cookie_life = timedelta(days=10.0)

TESTING = True
SECRET_KEY = secret_key
SQLALCHEMY_DATABASE_URI = database_url
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
PERMANENT_SESSION_LIFETIME = cookie_life
