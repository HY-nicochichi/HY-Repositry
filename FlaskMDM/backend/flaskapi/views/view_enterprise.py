from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import cors_enterprise
from helpers import manager_helper, enterprise_helper

bp_enterprise = Blueprint('bp_enterprise', __name__, url_prefix='/api/enterprise')

cors_enterprise.init_app(bp_enterprise)

@bp_enterprise.post('/create')
@jwt_required()
def create():
    identity = get_jwt_identity()
    client = manager_helper.get_client(identity)
    enterprise_token = request.json['enterprise_token']
    signup_url_name = request.json['signup_url_name']
    enterprise = enterprise_helper.create_enterprise(client, enterprise_token, signup_url_name)
    enterprise_name = enterprise['name']
    enterprise_helper.register(enterprise_name, identity)
    return jsonify({'enterprise_name': enterprise_name}), 200
