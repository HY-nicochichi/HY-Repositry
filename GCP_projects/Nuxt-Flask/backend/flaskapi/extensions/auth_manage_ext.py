from typing import Self
from datetime import datetime
from jwt import (
    encode,
    decode
)
from jwt.exceptions import (
    ExpiredSignatureError,
    InvalidTokenError
)
from flask import (
    Flask,
    request,
    session,
    current_app
)
from authlib.integrations.flask_client import OAuth

class AuthException(Exception):

    def __init__(self: Self, msg: str, status: int):
        self.msg = msg
        self.status = status

class AuthManager():

    def __init__(
        self: Self,
        app: Flask|None = None,
        cache = None,
        fetch_token = None,
        update_token = None
    ) -> None:
        self.oauth = OAuth()
        if app is not None:
            self.init_app(app, cache, fetch_token, update_token)

    def init_app(
        self: Self,
        app: Flask,
        cache = None,
        fetch_token = None,
        update_token = None
    ) -> None:
        self.oauth.init_app(app, cache, fetch_token, update_token)
        self.google = self.oauth.register(
            name = 'google',
            server_metadata_url = 'https://accounts.google.com/.well-known/openid-configuration',
            scope = 'openid email profile'
        )

        @app.errorhandler(AuthException)
        def auth_exception_handler(e: AuthException) -> tuple[dict, int]:
            return {'msg': e.msg}, e.status

        app.extensions['auth_manage_ext'] = self
    
    def client_domain(self: Self):
        client = session.pop('client', 'swagger_ui')
        domains = current_app.config['CLIENT_DOMAINS']
        if client not in domains:
            raise AuthException('Client not allowed', 400)
        return domains[client]

    def create_jwt(self: Self, user_info):
        payload = {
            'user_id': user_info.get('sub'),
            'email': user_info.get('email'),
            'name': user_info.get('name'),
            'exp': datetime.now() + current_app.config['JWT_EXPIRES']
        }
        return encode(
            payload,
            current_app.config['JWT_SECRET'],
            current_app.config['JWT_ALGORITHM']
        )

    def decode_jwt(self: Self, token: str|bytes):
        try:
            return decode(
                token,
                current_app.config['JWT_SECRET'],
                algorithms = [current_app.config['JWT_ALGORITHM']]
            )
        except (ExpiredSignatureError, InvalidTokenError):
            return None

    def user_info(self: Self):
        authorization = request.headers.get('Authorization')
        if not authorization or not authorization.startswith('Bearer '):
            raise AuthException('Authorization header is missing or invalid', 401)
        token = authorization.split(' ')[1]
        user_info = self.decode_jwt(token)
        if not user_info:
            raise AuthException('Token is expired or invalid', 401)
        return user_info
