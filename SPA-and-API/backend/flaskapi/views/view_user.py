from flask import (
    Blueprint,
    jsonify,
    request,
    Response
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
from helpers import user_helper
from models import User

bp_user = Blueprint('bp_user', __name__, url_prefix='/api/user')

@bp_user.post('/create')
def create() -> tuple[Response, int]:
    mail_address: str = request.json['mail_address']
    password: str = request.json['password']
    user_name: str = request.json['user_name']
    result: str = user_helper.create(mail_address, password, user_name)
    res_json: Response = jsonify({'msg': result})
    if result == '成功':
        return res_json, 200
    else:
        return res_json, 401

@bp_user.get('/info')
@jwt_required()
def info() -> tuple[Response, int]:
    identity: str = get_jwt_identity()
    current_user: User | None = user_helper.search_by_id(identity)
    if current_user:
        res_json: Response = jsonify({
            'mail_address': current_user.mail_address,
            'user_name': current_user.user_name
        })
        return res_json, 200
    else:
        res_json: Response = jsonify({'msg': 'ユーザーが存在しません'})
        return res_json, 401

@bp_user.post('/update')
@jwt_required()
def update() -> tuple[Response, int]:
    identity: str = get_jwt_identity()
    param: str = request.json['param']
    current_value: str = request.json['current_value']
    new_value: str = request.json['new_value']
    check_value: str = request.json['check_value']
    if param == 'メールアドレス':
        result: str = user_helper.update_mail_address(identity, current_value, new_value, check_value)
    elif param == 'パスワード':
        result: str = user_helper.update_password(identity, current_value, new_value, check_value)
    elif param == 'ユーザーネーム':
        result: str = user_helper.update_user_name(identity, current_value, new_value, check_value)
    res_json: Response = jsonify({'msg': result})
    if result == '成功':
        return res_json, 200
    else:
        return res_json, 401

@bp_user.get('/delete')
@jwt_required()
def delete() -> tuple[Response, int]:
    identity: str = get_jwt_identity()
    user_helper.delete(identity)
    res_json: Response = jsonify({'msg': '成功'})
    return res_json, 200
