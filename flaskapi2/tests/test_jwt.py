import pytest
from uuid import uuid4
from json import dumps
from flask.testing import FlaskClient
from werkzeug.security import generate_password_hash
from models import User
from . import (
    app,
    db_orm
)

JWT_API_ROUTE = '/jwt/'

def test_jwt_post() -> None:
    client: FlaskClient = app.test_client()
    sample_user = User(
        id = str(uuid4()),
        mail = 'foo',
        password_hash = generate_password_hash('foo'),
        name = 'foo'
    )
    # userテーブルにサンプルデータを用意
    with app.app_context():
        db_orm.session.add(sample_user)
        db_orm.session.commit()
    # 悪いリクエスト1(Content-Typeヘッダに誤り)
    bad_resp1 = client.post(
        JWT_API_ROUTE,
        data = dumps({
            'mail': 'foo',
            'password': 'foo'
        })
    )
    assert bad_resp1.status_code == 400
    assert bad_resp1.get_json()['msg'] == 'Content-TypeヘッダかJSONデータが誤っています'
    # 悪いリクエスト2(JSONデータに誤り)
    bad_resp2 = client.post(
        JWT_API_ROUTE,
        headers = {'Content-Type': 'application/json'},
        data = dumps({
            'mail': None,
            'password': ''
        })
    )
    assert bad_resp2.status_code == 400
    assert bad_resp2.get_json()['msg'] == 'Content-TypeヘッダかJSONデータが誤っています'
    # 悪いリクエスト3(存在しないメールアドレス)
    bad_resp3 = client.post(
        JWT_API_ROUTE,
        headers = {'Content-Type': 'application/json'},
        data = dumps({
           'mail': 'bar',
           'password': 'foo'
        })
    )
    assert bad_resp3.status_code == 401
    assert bad_resp3.get_json()['msg'] == 'メールアドレスが存在しません'
    # 悪いリクエスト4(誤ったパスワード)
    bad_resp4 = client.post(
        JWT_API_ROUTE,
        headers = {'Content-Type': 'application/json'},
        data = dumps({
            'mail': 'foo',
            'password': 'bar'
        })
    )
    assert bad_resp4.status_code == 401
    assert bad_resp4.get_json()['msg'] == 'パスワードが誤っています'
    # 良いリクエスト
    good_resp = client.post(
        JWT_API_ROUTE,
        headers = {'Content-Type': 'application/json'},
        data = dumps({
            'mail': 'foo',
            'password': 'foo'
        })
    )
    assert good_resp.status_code == 200
    assert 'access_token' in good_resp.get_json()
    # userテーブルをリセット
    with app.app_context():
        db_orm.session.delete(sample_user)
        db_orm.session.commit()
