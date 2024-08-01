from flask import Blueprint, jsonify, request
from extensions import cors_jwt
from helpers import JWTHelper, UserHelper

bp_jwt = Blueprint('bp_jwt', __name__, url_prefix='/api/jwt')

cors_jwt.init_app(bp_jwt)

@bp_jwt.post('/create')
def create():
    mail = request.json['mail']
    password = request.json['password']
    result = UserHelper.auth(mail, password)
    if result['message'] == '成功':
        access_token = JWTHelper.create(result['user_id'])
        res_json = jsonify({'access_token': access_token})
        return res_json, 200
    else:
        res_json = jsonify({'msg': result['message']})
        return res_json, 401
