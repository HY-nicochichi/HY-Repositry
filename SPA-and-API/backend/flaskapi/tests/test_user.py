import pytest
from time import sleep
from uuid import uuid4
from json import dumps
from flask.testing import FlaskClient
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
from models import User
from . import (
    app,
    db_orm
)

USER_API_ROUTE = '/user/'

def test_user_get() -> None:
    client: FlaskClient = app.test_client()
    sample_user = User(
        id = str(uuid4()),
        mail = 'foo',
        password_hash = generate_password_hash('foo'),
        name = 'foo'
    )
    # userテーブルにサンプルデータを用意 ＋ JWTを用意
    with app.app_context():
        db_orm.session.add(sample_user)
        db_orm.session.commit()
        bad_identity = str(uuid4())
        bad_jwt = create_access_token(identity=bad_identity)
        good_jwt = create_access_token(identity=sample_user.id)
    # 悪いリクエスト1(Authorizationヘッダに誤り)
    bad_resp1 = client.get(USER_API_ROUTE)
    assert bad_resp1.status_code == 401
    assert bad_resp1.get_json()['msg'] == 'Missing Authorization Header'
    # 悪いリクエスト2(存在しないユーザー情報のJWT)
    bad_resp2 = client.get(
        USER_API_ROUTE,
        headers = {'Authorization': f'Bearer {bad_jwt}'}
    )
    assert bad_resp2.status_code == 401
    assert bad_resp2.get_json()['msg'] == f'Error loading the user {bad_identity}'
    # 良いリクエスト
    good_resp = client.get(
        USER_API_ROUTE,
        headers = {'Authorization': f'Bearer {good_jwt}'}
    )
    assert good_resp.status_code == 200
    assert 'mail' in good_resp.get_json()
    assert 'name' in good_resp.get_json()
    # 悪いリクエスト3(期限切れのJWT)
    sleep(10)
    expired_jwt = good_jwt
    bad_resp3 = client.get(
        USER_API_ROUTE,
        headers = {'Authorization': f'Bearer {expired_jwt}'}
    )
    assert bad_resp3.status_code == 401
    assert bad_resp3.get_json()['msg'] == 'Token has expired'
    # userテーブルをリセット
    with app.app_context():
        db_orm.session.delete(sample_user)
        db_orm.session.commit()

def test_user_post() -> None:
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
    # 悪いリクエスト(既に存在するメールアドレス)
    bad_resp = client.post(
        USER_API_ROUTE,
        headers = {'Content-Type': 'application/json'},
        data = dumps({
            'mail': 'foo',
            'password': 'bar',
            'name': 'bar'
        })
    )
    assert bad_resp.status_code == 409
    assert bad_resp.get_json()['msg'] == 'メールアドレスの使用者が既に存在します'
    # 良いリクエスト
    good_resp = client.post(
        USER_API_ROUTE,
        headers = {'Content-Type': 'application/json'},
        data = dumps({
            'mail': 'bar',
            'password': 'bar',
            'name': 'bar'
        })
    )
    assert good_resp.status_code == 200
    assert good_resp.get_json()['msg'] == '登録しました'
    # userテーブルをリセット
    with app.app_context():
        db_orm.session.delete(sample_user)
        db_orm.session.delete(User.query.filter_by(mail='bar').first())
        db_orm.session.commit()

def test_user_put() -> None:
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
        jwt = create_access_token(identity=sample_user.id)
    # 悪いリクエスト1(誤った現メールアドレス)
    bad_resp1 = client.put(
        USER_API_ROUTE,
        headers = {
            'Authorization': f'Bearer {jwt}',
            'Content-Type': 'application/json'
        },
        data = dumps({
            'param': 'メールアドレス',
            'current_val': 'bar',
            'new_val': 'bar',
            'check_val': 'bar'
        })
    )
    assert bad_resp1.status_code == 404
    assert bad_resp1.get_json()['msg'] == '現メールアドレスが誤っています'
    # 悪いリクエスト2(新メールアドレスと確認用の不一致)
    bad_resp2 = client.put(
        USER_API_ROUTE,
        headers = {
            'Authorization': f'Bearer {jwt}',
            'Content-Type': 'application/json'
        },
        data = dumps({
            'param': 'メールアドレス',
            'current_val': 'foo',
            'new_val': 'bar',
            'check_val': 'foo'
        })
    )
    assert bad_resp2.status_code == 422
    assert bad_resp2.get_json()['msg'] == '新メールアドレスと確認用が一致しません'
    # 悪いリクエスト3(既に存在する新メールアドレス)
    bad_resp3 = client.put(
        USER_API_ROUTE,
        headers = {
            'Authorization': f'Bearer {jwt}',
            'Content-Type': 'application/json'
        },
        data = dumps({
            'param': 'メールアドレス',
            'current_val': 'foo',
            'new_val': 'foo',
            'check_val': 'foo'
        })
    )
    assert bad_resp3.status_code == 409
    assert bad_resp3.get_json()['msg'] == '新メールアドレスの使用者が既に存在します'
    # 良いリクエスト1(メールアドレス)
    good_resp1 = client.put(
        USER_API_ROUTE,
        headers = {
            'Authorization': f'Bearer {jwt}',
            'Content-Type': 'application/json'
        },
        data = dumps({
            'param': 'メールアドレス',
            'current_val': 'foo',
            'new_val': 'bar',
            'check_val': 'bar'
        })
    )
    assert good_resp1.status_code == 200
    assert good_resp1.get_json()['msg'] == 'メールアドレスを変更しました'
    # 悪いリクエスト4(誤った現パスワード)
    bad_resp4 = client.put(
        USER_API_ROUTE,
        headers = {
            'Authorization': f'Bearer {jwt}',
            'Content-Type': 'application/json'
        },
        data = dumps({
            'param': 'パスワード',
            'current_val': 'bar',
            'new_val': 'bar',
            'check_val': 'bar'
        })
    )
    assert bad_resp4.status_code == 404
    assert bad_resp4.get_json()['msg'] == '現パスワードが誤っています'
    # 良いリクエスト2(パスワード)
    good_resp2 = client.put(
        USER_API_ROUTE,
        headers = {
            'Authorization': f'Bearer {jwt}',
            'Content-Type': 'application/json'
        },
        data = dumps({
            'param': 'パスワード',
            'current_val': 'foo',
            'new_val': 'bar',
            'check_val': 'bar'
        })
    )
    assert good_resp2.status_code == 200
    assert good_resp2.get_json()['msg'] == 'パスワードを変更しました'
    # 良いリクエスト3(ユーザーネーム)
    good_resp3 = client.put(
        USER_API_ROUTE,
        headers = {
            'Authorization': f'Bearer {jwt}',
            'Content-Type': 'application/json'
        },
        data = dumps({
            'param': 'ユーザーネーム',
            'current_val': 'foo',
            'new_val': 'bar',
            'check_val': 'bar'
        })
    )
    assert good_resp3.status_code == 200
    assert good_resp3.get_json()['msg'] == 'ユーザーネームを変更しました'
    # userテーブルをリセット
    with app.app_context():
        db_orm.session.delete(User.query.filter_by(mail='bar').first())
        db_orm.session.commit()

def test_user_delete() -> None:
    client: FlaskClient = app.test_client()
    sample_user = User(
        id = str(uuid4()),
        mail = 'foo',
        password_hash = generate_password_hash('foo'),
        name = 'foo'
    )
    # userテーブルにサンプルデータを用意 ＋ JWTを用意
    with app.app_context():
        db_orm.session.add(sample_user)
        db_orm.session.commit()
        jwt = create_access_token(identity=sample_user.id)
    # 良いリクエスト
    good_resp = client.delete(
        USER_API_ROUTE,
        headers = {'Authorization': f'Bearer {jwt}'}
    )
    assert good_resp.status_code == 200
    assert good_resp.get_json()['msg'] == '退会しました'
