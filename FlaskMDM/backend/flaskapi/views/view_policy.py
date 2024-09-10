from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import cors_policy
from helpers import manager_helper, policy_helper

bp_policy = Blueprint('bp_policy', __name__, url_prefix='/api/policy')

cors_policy.init_app(bp_policy)

@bp_policy.post('/create')
@jwt_required()
def create():
    enterprise_name = request.json['enterprise_name']
    policy_name = request.json['policy_name']
    message = policy_helper.register(enterprise_name, policy_name)
    if message != '成功':
        return jsonify({'msg': message}), 401
    else:
        identity = get_jwt_identity()
        client = manager_helper.get_client(identity)
        policy_json = request.json['policy_json']
        enrollment_token = policy_helper.get_enrollment_token(
            client, enterprise_name, policy_name, policy_json
        )
        enrollment_link = f'https://enterprise.google.com/android/enroll?et={enrollment_token['value']}'
        return jsonify({'enrollment_link': enrollment_link}), 200
