from datetime import timedelta

# 以下の２項目は本番ではAWSのSecretManager等で厳重保管すべし
secret_key = 'Flask_Market_Secret_Key'
database_url = 'postgresql+psycopg2://postgres:password@db:5432/postgres'

cookie_life = timedelta(days=10.0)

TESTING = True
SCHEDULER_API_ENABLED = True
SECRET_KEY = secret_key
SQLALCHEMY_DATABASE_URI = database_url
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SERVER_SESSION = {
    'session.type': 'ext:database',
    'session.url': database_url,
    'session.cookie_expires': cookie_life,
    'session.secret': secret_key,
    'session.encrypt_key': secret_key,
    'session.validate_key': secret_key,
}
SECURITY_HEADER = {
    'content_security_policy': {
        'default-src': [
            "'self'",
            "'unsafe-eval'",
            'stackpath.bootstrapcdn.com',
            'code.jquery.com',
            'cdn.jsdelivr.net'
        ]
    },
    'content_security_policy_nonce_in': [
        'default-src'
    ]
}
