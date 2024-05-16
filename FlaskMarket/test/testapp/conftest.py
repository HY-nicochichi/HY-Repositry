from uuid import uuid4
from pytest import fixture
from contextlib import contextmanager
from werkzeug.security import generate_password_hash
from coreApp import create_app
from extensions import db_orm
from models import User, Item

@fixture
def client():
    app = create_app()
    with app.app_context():
        db_orm.create_all()     
        test_user_01 = User(
            user_id = str(uuid4()),
            mail = 'test01@flaskmail.com',
            hashPASS = generate_password_hash('TestPass01'),
            username = 'TestUserName01'
        )
        test_item_01 = Item(
            item_id = str(uuid4()),
            itemname = 'TestItemName01',
            price = 300,
            stock = 30,
            tag = 'fish',
            seller = test_user_01.user_id
        )
        db_orm.session.add(test_user_01)
        db_orm.session.add(test_item_01)
        db_orm.session.commit()
        with app.test_client() as client:
            yield client
        db_orm.session.delete(test_user_01)
        db_orm.session.delete(test_item_01)
        db_orm.session.commit()

@contextmanager
def session_transaction(client):
    with client.session_transaction() as session:
        session.clear()
        session.permanent = True
        yield session
