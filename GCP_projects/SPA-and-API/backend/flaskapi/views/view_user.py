from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from extensions import cors_user
from helpers import JWTHelper, UserHelper

bp_user = Blueprint('bp_user', __name__, url_prefix='/api/user')

cors_user.init_app(bp_user)

@bp_user.post('/create')
def create():
    mail = request.json['mail']
    password = request.json['password']
    username = request.json['username']
    result = UserHelper.register(mail, password, username)
    res_json = jsonify({'msg': result['message']})
    if result['message'] == '成功':
        return res_json, 200
    else:
        return res_json, 401

@bp_user.get('/info')
@jwt_required()
def info():
    identity = JWTHelper.get_identity()
    current_user = UserHelper.search_by_id(identity)
    if current_user:
        user_info = {
            'mail': current_user.mail,
            'username': current_user.username
        }
        res_json = jsonify({'user_info': user_info})
        return res_json, 200
    else:
        res_json = jsonify({'msg': 'ユーザーが存在しません'})
        return res_json, 401

@bp_user.post('/update')
@jwt_required()
def update():
    identity = JWTHelper.get_identity()
    param = request.json['param']
    current_value = request.json['current_value']
    new_value = request.json['new_value']
    check_value = request.json['check_value']
    if param == 'メールアドレス':
        result = UserHelper.update_mail(identity, current_value, new_value, check_value)
    elif param == 'パスワード':
        result = UserHelper.update_password(identity, current_value, new_value, check_value)
    elif param == 'ユーザーネーム':
        result = UserHelper.update_username(identity, current_value, new_value, check_value)
    res_json = jsonify({'msg': result})
    if result == '成功':
        return res_json, 200
    else:
        return res_json, 401

@bp_user.get('/delete')
@jwt_required()
def delete():
    identity = JWTHelper.get_identity()
    UserHelper.delete(identity)
    res_json = jsonify({'msg': '成功'})
    return res_json, 200
