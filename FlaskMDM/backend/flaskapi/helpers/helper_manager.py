from werkzeug.security import generate_password_hash, check_password_hash
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from models import Manager
from extensions import db_orm

class ManagerHelper():

    def search_by_manager_id(self, manager_id):
        return Manager.query.filter_by(manager_id=manager_id).one_or_none()

    def authenticate(self, manager_id, password):
        if manager_id == 'Admin' and password == 'Admin':
            return '成功'
        else:
            found_manager = ManagerHelper.search_by_manager_id(manager_id)
            if found_manager == None:
                return 'マネージャーIDが存在しません'
            elif check_password_hash(found_manager.hashPASS, password) == False:
                return 'パスワードが誤っています'
            else:
                return '成功'

    def register(self, manager_id, password):
        if ManagerHelper.search_by_manager_id(manager_id):
            return 'マネージャーIDが既に存在します'
        else:
            hashPASS = generate_password_hash(password)
            new_manager = Manager(manager_id=manager_id, hashPASS=hashPASS)
            db_orm.session.add(new_manager)
            db_orm.session.commit()
            return '成功'

    def get_client(self, manager_id):
        service_account_file = f'/manager_keys/{manager_id}.json'
        credentials = Credentials.from_service_account_file(
            service_account_file, scopes=['https://www.googleapis.com/auth/androidmanagement']
        )
        return build('androidmanagement', 'v1', credentials=credentials)

    def get_signup_url(self, client):
        signup_url = client.signupUrls().create(
            projectId = 'flaskmdm',
            callbackUrl = 'https://storage.googleapis.com/android-management-quick-start/enterprise_signup_callback.html'
        ).execute()
        return signup_url

    def create_service_account_file(self, manager_id, service_account_json):
        split_parts = service_account_json.split('\n')
        num = len(split_parts)
        with open(f'/manager_keys/{manager_id}.json', 'w') as file_ctx:
            for i in range(num):
                if i == num-1:
                    file_ctx.write(split_parts[i])
                elif i >= 4 and i <= num-10:
                    file_ctx.write(split_parts[i])
                    file_ctx.write('\\')
                    file_ctx.write('n')
                else:
                    file_ctx.write(f'{split_parts[i]}\n')
        return f'{manager_id}.json'
