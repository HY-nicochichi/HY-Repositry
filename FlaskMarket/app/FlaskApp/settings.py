from datetime import timedelta

# 以下の３項目はAWSのSecretManager等で厳重に保管すべし
secret_key = 'Flask_Market_Secret_Key'
database_url = 'sqlite:///db.sqlite3'
session_url = 'sqlite:///instance/db.sqlite3'

cookie_life = timedelta(days=15.0)
session_timeout = 5

TESTING = True
SCHEDULER_API_ENABLED = True
SECRET_KEY = secret_key
SQLALCHEMY_DATABASE_URI = database_url
SQLALCHEMY_TRACK_MODIFICATIONS = False
BEAKER_SESSION = {
    'session.key': 'session_id',
    'session.type': 'ext:database',
    'session.url': session_url,
    'session.table_name': 'sessions',
    'session.httponly': True,
    'session.cookie_expires': cookie_life,
    'session.timeout': int(session_timeout) *(60*60*24),
    'session.auto': True,
    'session.secret': secret_key,
    'session.encrypt_key': secret_key,
    'session.validate_key': secret_key,
}
