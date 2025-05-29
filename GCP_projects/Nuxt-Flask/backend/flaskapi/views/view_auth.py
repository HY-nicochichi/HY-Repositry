from flask import (
    Blueprint,
    Response,
    request,
    url_for,
    redirect,
    session
)
from extensions import auth_manager
from authlib.common.security import generate_token

bp_auth = Blueprint('bp_auth', __name__, url_prefix='/auth')

@bp_auth.get('/')
def auth_get() -> tuple[Response, int]: 
    session['client'] = request.args.get(
        'client', type=str, default='swagger_ui'
    ) 
    redirect_response = auth_manager.google.authorize_redirect(
        redirect_uri = url_for('bp_auth.auth_callback_get', _external=True),
        prompt = 'select_account'
    )
    return redirect_response, 302

@bp_auth.get('/callback')
def auth_callback_get() -> tuple[Response, int]:
    domain = auth_manager.client_domain()
    try:
        token = auth_manager.google.authorize_access_token()
    except Exception:
        return redirect(f'{domain}?msg=google_auth_failed'), 302
    user_info = token.get('userinfo')
    if not user_info:
        return redirect(f'{domain}/?msg=user_info_missing'), 302
    jwt_token = auth_manager.create_jwt(user_info)
    token_key = generate_token(32)
    session[f'token_{token_key}'] = jwt_token
    return redirect(f'{domain}?msg=success&token_key={token_key}'), 302

@bp_auth.post('/token')
def auth_token_post() -> tuple[dict, int]:
    token_key = request.json.get('token_key', '')
    jwt_token = session.pop(f'token_{token_key}', None)
    if not jwt_token:
        return {'msg': 'Failed to get access token'}, 400
    else:
        return {'access_token': jwt_token}, 200
