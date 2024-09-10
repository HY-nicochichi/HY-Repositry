from models import Enterprise
from extensions import db_orm

class EnterpriseHelper():

    def search_by_enterprise_name(self, enterprise_name):
        return Enterprise.query.filter_by(enterprise_name=enterprise_name).one_or_none()

    def search_by_manager_id(self, manager_id):
        return Enterprise.query.filter_by(manager_id=manager_id).all()

    def register(self, enterprise_name, manager_id):
        new_enterprise = Enterprise(enterprise_neme=enterprise_name, manager_id=manager_id)
        db_orm.session.add(new_enterprise)
        db_orm.session.commit()

    def create_enterprise(self, client, enterprise_token, signup_url_name):
        enterprise = client.enterprises().create(
            projectId = 'flaskmdm',
            signupUrlName = signup_url_name,
            enterpriseToken = enterprise_token,
            body = {}
        ).execute()
        return enterprise
