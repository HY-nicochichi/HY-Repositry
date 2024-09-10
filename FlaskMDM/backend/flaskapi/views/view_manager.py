from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import cors_manager
from helpers import manager_helper, enterprise_helper

bp_manager = Blueprint('bp_manager', __name__, url_prefix='/api/manager')

cors_manager.init_app(bp_manager)

@bp_manager.post('/create')
@jwt_required()
def create():
    identity = get_jwt_identity()
    if identity != 'Admin':
        return jsonify({'msg': '貴方はAdminではありません'}), 401
    else:
        manager_id = request.json['manager_id']
        password = request.json['password']
        message = manager_helper.register(manager_id, password)
        if message != '成功':
            return jsonify({'msg': message}), 401
        else:
            service_account_json = request.json['service_account_json']
            file_name = manager_helper.create_service_account_file(
                manager_id, service_account_json
            )
            return jsonify({'msg': f'マネージャーの登録と{file_name}の作成に成功'}), 200

@bp_manager.get('/info')
@jwt_required()
def info():
    identity = get_jwt_identity()
    if manager_helper.search_by_manager_id(identity) == None: 
        return jsonify({'msg': 'ユーザーが存在しません'}), 401
    else:
        enterprises = enterprise_helper.search_by_manager_id(identity)
        enterprise_name_list = []
        for enterprise in enterprises:
            enterprise_name_list.append(enterprise.enterprise_name)
        res_json = jsonify({
            'manager_id': identity,
            'enterprises': enterprise_name_list
        })
        return res_json, 200

@bp_manager.get('/signup')
@jwt_required()
def signup():
    identity = get_jwt_identity()
    signup_url = manager_helper.get_signup_url(identity)
    res_json = jsonify({
        'signup': {
            'url': signup_url['url'],
            'name': signup_url['name']
        }
    })
    return res_json, 200
