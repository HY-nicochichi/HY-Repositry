from conftest import client, session_transaction
from helpers import UserHelper

def test_index_GET(client):
    # check1
    with session_transaction(client):
        pass
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert response.json['user_info']['login'] == False
    # check2
    user_id = UserHelper.search_by_mail('test01@flaskmail.com').user_id
    with session_transaction(client) as session:
        session['user'] = user_id
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert response.json['user_info']['login'] == True

def test_login_GET(client):
    # check1
    with session_transaction(client):
        pass
    response = client.get('/login', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/login'
    # check2
    user_id = UserHelper.search_by_mail('test01@flaskmail.com').user_id
    with session_transaction(client) as session:
        session['user'] = user_id
        session['basket'] = {}
    response = client.get('/login', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/'
    assert response.json['user_info']['login'] == True
    assert response.json['user_info']['name'] == 'TestUserName01'

def test_login_POST(client):
    # check1
    with session_transaction(client):
        pass
    response = client.post(
        '/login',
        follow_redirects=True,
        data = {
            'mail': 'test01@flaskmail.com',
            'password': 'TestPass01'
        }
    )
    assert response.status_code == 200
    assert response.request.path == '/'
    assert response.json['user_info']['login'] == True
    assert response.json['user_info']['name'] == 'TestUserName01'
    # check2
    with session_transaction(client):
        pass
    response = client.post(
        '/login',
        follow_redirects=True,
        data = {
            'mail': 'wrong@flaskmail.com',
            'password': 'TestPass01'
        }
    )
    assert response.status_code == 200
    assert response.request.path == '/login'
    assert response.json['user_info']['login'] == False
    # check3
    with session_transaction(client):
        pass
    response = client.post(
        '/login',
        follow_redirects=True,
        data = {
            'mail': 'test01@flaskmail.com',
            'password': 'WrongPass'
        }
    )
    assert response.status_code == 200
    assert response.request.path == '/login'
    assert response.json['user_info']['login'] == False
    # check4
    user_id = UserHelper.search_by_mail('test01@flaskmail.com').user_id
    with session_transaction(client) as session:
        session['user'] = user_id
    response = client.post(
        '/login',
        follow_redirects=True,
        data = {
            'mail': 'wrong@flaskmail.com',
            'password': 'WrongPass'
        }
    )
    assert response.status_code == 200
    assert response.request.path == '/'
    assert response.json['user_info']['login'] == True
    assert response.json['user_info']['name'] == 'TestUserName01'

def test_logout_GET(client):
    # check1
    with session_transaction(client):
        pass
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/login'
    # check2
    user_id = UserHelper.search_by_mail('test01@flaskmail.com').user_id
    with session_transaction(client) as session:
        session['user'] = user_id
        session['basket'] = {}
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/'
    assert response.json['user_info']['login'] == False
