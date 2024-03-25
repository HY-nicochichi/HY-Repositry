from google.cloud.secretmanager import SecretManagerServiceClient
from google.cloud.sql.connector import Connector, IPTypes
from json import loads
from datetime import timedelta
from os import environ

environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/flaskmarket/fake_service_account_key.json'

SM_client = SecretManagerServiceClient()
connector = Connector(ip_type=IPTypes.PUBLIC)

name = SM_client.secret_version_path('project_id', 'secret_name', 'latest')
response = SM_client.access_secret_version(name=name)
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

cookie_life = timedelta(days=15.0)
session_timeout = 5
session_time_info = {
    'cookie_life': cookie_life,
    'session_timeout': timedelta(days=float(session_timeout))
}

SCHEDULER_API_ENABLED = True
SECRET_KEY = secret_key
SQLALCHEMY_DATABASE_URI = database_url
SQLALCHEMY_ENGINE_OPTIONS = {'creator': creator}
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
BEAKER_SESSION = {
    'session.key': 'session_id',
    'session.type': 'ext:database',
    'session.sa_opts': {'sa.url': database_url, 'sa.creator': creator},
    'session.table_name': 'sessions',
    'session.httponly': True,
    'session.cookie_expires': cookie_life,
    'session.timeout': session_timeout *(60*60*24),
    'session.auto': True,
    'session.secret': secret_key,
    'session.encrypt_key': secret_key,
    'session.validate_key': secret_key,
}
