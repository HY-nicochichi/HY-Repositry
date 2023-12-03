from flask import session
import pytest
from coreApp import app

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_index(client):
    with client:
        response = client.get('/')
        assert response.status_code == 200
        assert 'user' not in session
