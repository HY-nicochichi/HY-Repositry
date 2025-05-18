from jwt import decode
from flask import (
    Blueprint,
    request,
)
from extensions import auth_manager

bp_auth = Blueprint('bp_auth', __name__, url_prefix='/auth')

@bp_auth.get('/to-google')
def to_google() -> tuple[dict, int]:
    url, state = auth_manager.google.authorize_redirect(
        request.url_root + '/auth/from-google'
    )
    return {'url': url, 'state': state}, 200

@bp_auth.get('/from-google')
def from_google() -> tuple[dict, int]:
    token = auth_manager.google.authorize_access_token()
    if not token:
        return {'msg': 'Failed to retrieve access token'}, 400
    user_info = token.get('userinfo')
    if not user_info:
        id_token = token.get('id_token')
        if id_token:
            try:
                claims = decode(
                    id_token,
                    auth_manager.google.client_secret,
                    algorithms = ['RS256'],
                    audience = auth_manager.google.client_id
                )
                user_info = {
                    'sub': claims.get('sub'),
                    'email': claims.get('email'),
                    'name': claims.get('name')
                }
            except:
                return {'msg': 'Failed to decode ID-token'}, 400
        else:
            return {'msg': 'No user-info or ID-token'}, 400
    access_token = auth_manager.create_jwt(user_info)
    return {'acsess_token': access_token}, 200
