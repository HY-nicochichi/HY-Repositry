from conftest import client, session_transaction
from helpers import UserHelper

def test_new_user_GET(client):
    # check1
    with session_transaction(client):
        pass
    response = client.get('/new_user', follow_redirects=True)
    assert response.status_code == 200
    assert response.json['user_info']['login'] == False
    assert response.request.path == '/new_user'
    # check2
    user_id = UserHelper.search_by_mail('test01@flaskmail.com').user_id
    with session_transaction(client) as session:
        session['user'] = user_id
    response = client.get('/new_user', follow_redirects=True)
    assert response.status_code == 200
    assert response.json['user_info']['login'] == True
    assert response.request.path == '/'
