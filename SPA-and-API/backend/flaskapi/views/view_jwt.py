from flask import (
    Blueprint,
    jsonify,
    request,
    Response
)
from flask_jwt_extended import create_access_token
from helpers import user_helper

bp_jwt = Blueprint('bp_jwt', __name__, url_prefix='/api/jwt')

@bp_jwt.post('/create')
def create() -> tuple[Response, int]:
    mail_address: str = request.json['mail_address']
    password: str = request.json['password']
    result: dict[str, str] = user_helper.authenticate(mail_address, password)
    if result['msg'] == '成功':
        access_token: str = create_access_token(identity=result['user_id'])
        res_json: Response = jsonify({'access_token': access_token})
        return res_json, 200
    else:
        res_json: Response = jsonify({'msg': result['msg']})
        return res_json, 401
