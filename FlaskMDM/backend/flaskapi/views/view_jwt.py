from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from extensions import cors_jwt
from helpers import manager_helper

bp_jwt = Blueprint('bp_jwt', __name__, url_prefix='/api/jwt')

cors_jwt.init_app(bp_jwt)

@bp_jwt.post('/create')
def create():
    manager_id = request.json['manager_id']
    password = request.json['password']
    message = manager_helper.authenticate(manager_id, password)
    if message != '成功':
        res_json = jsonify({'msg': message})
        return res_json, 401
    else:
        access_token = create_access_token(identity=manager_id)
        res_json = jsonify({'access_token': access_token})
        return res_json, 200
