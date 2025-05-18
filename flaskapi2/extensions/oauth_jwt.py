from typing import Self
from datetime import datetime
from jwt import encode, decode
from jwt.exceptions import (
    ExpiredSignatureError,
    InvalidTokenError
)
from flask import Flask, request
from authlib.integrations.flask_client import OAuth

class AuthException(Exception):

    def __init__(self: Self, msg: str|None = None):
        self.msg = msg

class OAuthJWT(OAuth):

    def __init__(
        self: Self,
        app: Flask|None = None,
        cache = None,
        fetch_token = None,
        update_token = None
    ) -> None:
        if app is not None:
            self.init_app(app, cache, fetch_token, update_token)

    def init_app(
        self: Self,
        app: Flask,
        cache = None,
        fetch_token = None,
        update_token = None
    ) -> None:
        super().init_app(app, cache, fetch_token, update_token)
        self.google = self.register(
            name = 'google',
            client_id = app.config['JWT_CONFIG'],
            client_secret = app.config['JWT_CONFIG'],
            authorize_url = 'https://accounts.google.com/o/oauth2/auth',
            access_token_url = 'https://oauth2.googleapis.com/token',
            userinfo_endpoint = 'https://openidconnect.googleapis.com/v1/userinfo',
            scope = 'openid email profile'
        )

        @app.handle_exception(AuthException)
        def auth_excption_handler(e: AuthException) -> tuple[dict, int]:
            return {'msg': e.msg}, 401

    def create_jwt(self: Self, user_info):
        payload = {
            'user_id': user_info.get('sub'),
            'email': user_info.get('email'),
            'name': user_info.get('name'),
            'exp': datetime.now() + self.app.config['JWT_EXPIRES']
        }
        return encode(
            payload,
            self.app.config['JWT_SECRET_KEY'],
            self.app.config['JWT_ALGORITHM']
        )

    def decode_jwt(self: Self, token: str|bytes):
        try:
            return decode(
                token,
                self.app.config['JWT_SECRET_KEY'],
                algorithms = [self.app.config['JWT_ALGORITHM']]
            )
        except ExpiredSignatureError:
            return None
        except InvalidTokenError:
            return None
        
    def user_info(self: Self):
        authorization = request.headers.get('Authorization')
        if not authorization or not authorization.startswith('Bearer '):
            return AuthException('Authorization header is missing or invalid')
        token = authorization.split(' ')[1]
        user_data = self.decode_jwt(token)
        if not user_data:
            return AuthException('Token is expired or invalid')
        return user_data
