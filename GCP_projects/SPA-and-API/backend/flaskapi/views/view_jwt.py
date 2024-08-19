from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from extensions import cors_jwt
from helpers import user_helper

bp_jwt = Blueprint('bp_jwt', __name__, url_prefix='/api/jwt')

cors_jwt.init_app(bp_jwt)

@bp_jwt.post('/create')
def create():
    mail = request.json['mail']
    password = request.json['password']
    result = user_helper.authenticate(mail, password)
    if result['msg'] == '成功':
        access_token = create_access_token(result['user_id'])
        res_json = jsonify({'access_token': access_token})
        return res_json, 200
    else:
        res_json = jsonify({'msg': result['msg']})
        return res_json, 401
