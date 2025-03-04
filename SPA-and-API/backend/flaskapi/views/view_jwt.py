from pydantic import ValidationError
from flask import (
    Blueprint,
    jsonify,
    request,
    Response
)
from flask_jwt_extended import create_access_token
from helpers import user_helper
from models import JWTPost

bp_jwt = Blueprint('bp_jwt', __name__, url_prefix='/jwt')

@bp_jwt.post('/')
def jwt_post() -> tuple[Response, int]:
    try:
        data: JWTPost = JWTPost.model_validate(request.get_json(silent=True))
    except (TypeError, ValidationError):
        resp: Response = jsonify({'msg': 'Content-TypeヘッダかJSONデータが誤っています'})
        return resp, 400
    result: dict[str, str] = user_helper.authenticate(data)
    if result['msg'] == '成功':
        access_token: str = create_access_token(identity=result['user_id'])
        resp: Response = jsonify({'access_token': access_token})
        return resp, 200
    else:
        resp: Response = jsonify({'msg': result['msg']})
        return resp, 401
