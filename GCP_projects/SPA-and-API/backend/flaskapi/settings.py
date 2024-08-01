from google.cloud.secretmanager import SecretManagerServiceClient
from google.cloud.sql.connector import Connector, IPTypes
from json import loads
from datetime import timedelta
from os import environ

environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/fake_service_account_key.json'

client = SecretManagerServiceClient()
connector = Connector(ip_type=IPTypes.PUBLIC)

name = client.secret_version_path('project_id', 'secret_name', 'latest')
response = client.access_secret_version(name=name)
secret_dict = loads(response.payload.data.decode('UTF-8'))

creator_info = secret_dict['database']['creator']

def creator():
    connection = connector.connect(
        creator_info['connection_name'],
        creator_info['driver'],
        user=creator_info['user'],
        password=creator_info['password'],
        db=creator_info['db_name']
    )
    return connection

# utf-8
JSON_AS_ASCII = False

# db_orm
SQLALCHEMY_DATABASE_URI = secret_dict['database']['url']
SQLALCHEMY_ENGINE_OPTIONS = {'creator': creator}
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# jwt_manager
JWT_SECRET_KEY = secret_dict['secret_key']
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7.0)
