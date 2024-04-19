from google.cloud.secretmanager import SecretManagerServiceClient
from google.cloud.sql.connector import Connector, IPTypes
from json import loads
from datetime import timedelta
from os import environ

environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/fake_service_account_key.json'

client = SecretManagerServiceClient()
connector = Connector(ip_type=IPTypes.PUBLIC)

name = client.secret_version_path('project_id', 'secret_name', 'version')
response = client.access_secret_version(name=name)
secret_dict = loads(response.payload.data.decode('UTF-8'))

secret_key = secret_dict['secret_key']
database_url = secret_dict['database']['url']
connect_info = secret_dict['database']['connect_info']

def creator():
    connection = connector.connect(
        connect_info['connection_name'],
        connect_info['driver'],
        user=connect_info['user'],
        password=connect_info['password'],
        db=connect_info['db_name']
    )
    return connection

cookie_life = timedelta(days=10.0)

SCHEDULER_API_ENABLED = True
SECRET_KEY = secret_key
SQLALCHEMY_DATABASE_URI = database_url
SQLALCHEMY_ENGINE_OPTIONS = {'creator': creator}
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SERVER_SESSION = {
    'session.type': 'ext:database',
    'session.sa_opts': {'sa.url': database_url, 'sa.creator': creator},
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
