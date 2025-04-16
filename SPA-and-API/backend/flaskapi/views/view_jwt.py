from pydantic import ValidationError
from flask import (
    Blueprint,
    request
)
from flask_jwt_extended import create_access_token
from helpers import user_helper
from models import JWTPost

bp_jwt = Blueprint('bp_jwt', __name__, url_prefix='/jwt')

@bp_jwt.post('/')
def jwt_post() -> tuple[dict, int]:
    try:
        data: JWTPost = JWTPost.model_validate(request.get_json(silent=True))
    except (TypeError, ValidationError):
        return {'msg': 'Content-TypeヘッダかJSONデータが誤っています'}, 400
    result: dict[str, str] = user_helper.authenticate(data)
    if result['msg'] == '成功':
        access_token: str = create_access_token(identity=result['id'])
        return {'access_token': access_token}, 200
    else:
        return {'msg': result['msg']}, 401
