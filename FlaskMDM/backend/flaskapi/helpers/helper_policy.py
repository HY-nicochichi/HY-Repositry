from json import loads
from models import Policy
from extensions import db_orm

class PolicyHelper():

    def search_by_policy_name(self, policy_name):
        return Policy.query.filter_by(policy_name=policy_name).one_or_none()

    def search_by_enterprise_name(self, enterprise_name):
        return Policy.query.filter_by(enterprise_name=enterprise_name).all()

    def register(self, enterprise_name, policy_name):
        if PolicyHelper.search_by_policy_name(policy_name):
            return 'ポリシーネームが既に存在します'
        else:
            new_policy = Policy(policy_name=policy_name, enterprise_name=enterprise_name)
            db_orm.session.add(new_policy)
            db_orm.session.commit()
            return '成功'

    def get_enrollment_token(self, client, enterprise_name, policy_name, policy_json):
        name = f'{enterprise_name}/policies/{policy_name}'
        client.enterprises().policies().patch(
            name = name,
            body = loads(policy_json)
        ).execute()
        enrollment_token = client.enterprises().enrollmentTokens().create(
            parent = enterprise_name,
            body = {'policyName': name}
        ).execute()
        return enrollment_token
