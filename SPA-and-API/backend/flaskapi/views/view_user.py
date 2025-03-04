from pydantic import ValidationError
from flask import (
    Blueprint,
    jsonify,
    request,
    Response
)
from flask_jwt_extended import (
    jwt_required,
    current_user
)
from helpers import user_helper
from models import (
    UserPost,
    UserPut
)

bp_user = Blueprint('bp_user', __name__, url_prefix='/user')

@bp_user.get('/')
@jwt_required()
def user_get() -> tuple[Response, int]:
    resp: Response = jsonify({
        'mail': current_user.mail,
        'name': current_user.name
    })
    return resp, 200

@bp_user.post('/')
def user_post() -> tuple[Response, int]:
    try:
        data: UserPost = UserPost.model_validate(request.get_json(silent=True))
    except (TypeError, ValidationError):
        resp: Response = jsonify({'msg': 'Content-TypeヘッダかJSONデータが誤っています'})
        return resp, 400
    result: str = user_helper.create(data)
    if result == '成功':
        resp: Response = jsonify({'msg': '登録しました'})
        return resp, 200
    else:
        resp: Response = jsonify({'msg': result})
        return resp, 409

@bp_user.put('/')
@jwt_required()
def user_put() -> tuple[Response, int]:
    try:
        data: UserPut = UserPut.model_validate(request.get_json(silent=True))
    except (TypeError, ValidationError):
        resp: Response = jsonify({'msg': 'Content-TypeヘッダかJSONデータが誤っています'})
        return resp, 400
    match data.param:
        case 'メールアドレス':
            result: dict[str, str | int] = user_helper.update_mail_address(current_user.id, data)
        case 'パスワード':
            result: dict[str, str | int] = user_helper.update_password(current_user.id, data)
        case 'ユーザーネーム':
            result: dict[str, str | int] = user_helper.update_user_name(current_user.id, data)    
    if result['msg'] == '成功':
        resp: Response = jsonify({'msg': f'{data.param}を変更しました'})
        return resp, 200
    else:
        resp: Response = jsonify({'msg': result['msg']})
        status: int = result['status']
        return resp, status

@bp_user.delete('/')
@jwt_required()
def user_delete() -> tuple[Response, int]:
    user_helper.delete(current_user.id)
    resp: Response = jsonify({'msg': '退会しました'})
    return resp, 200
