from pydantic import ValidationError
from flask import (
    Blueprint,
    request
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
def user_get() -> tuple[dict, int]:
    return {'mail': current_user.mail, 'name': current_user.name}, 200

@bp_user.post('/')
def user_post() -> tuple[dict, int]:
    try:
        data: UserPost = UserPost.model_validate(request.get_json(silent=True))
    except (TypeError, ValidationError):
        return {'msg': 'Content-TypeヘッダかJSONデータが誤っています'}, 400
    result: str = user_helper.create(data)
    if result == '成功':
        return {'msg': '登録しました'}, 200
    else:
        return {'msg': result}, 409

@bp_user.put('/')
@jwt_required()
def user_put() -> tuple[dict, int]:
    try:
        data: UserPut = UserPut.model_validate(request.get_json(silent=True))
    except (TypeError, ValidationError):
        return {'msg': 'Content-TypeヘッダかJSONデータが誤っています'}, 400
    match data.param:
        case 'メールアドレス':
            result: dict[str, str|int] = user_helper.update_mail(data)
        case 'パスワード':
            result: dict[str, str|int] = user_helper.update_password(data)
        case 'ユーザーネーム':
            result: dict[str, str|int] = user_helper.update_name(data)    
    if result['msg'] == '成功':
        return {'msg': f'{data.param}を変更しました'}, 200
    else:
        return {'msg': result['msg']}, result['status']

@bp_user.delete('/')
@jwt_required()
def user_delete() -> tuple[dict, int]:
    user_helper.delete()
    return {'msg': '退会しました'}, 200
