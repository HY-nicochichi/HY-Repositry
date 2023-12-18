from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
from extensions import db, BaseModel

class User(BaseModel):

    __tablename__ = 'users'

    id = db.Column(db.String(255), primary_key=True, nullable=False)
    mail = db.Column(db.String(255), unique=True, nullable=False)
    hashPASS = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)

    def search_by_id(id):
        found_user = User.query.filter_by(id=str(id)).first()
        return found_user
    
    def search_by_mail(mail):
        found_user = User.query.filter_by(mail=str(mail)).first()
        return found_user

    def register(mail, password, username):
        result = {}
        if User.search_by_mail(mail) != None:
            result['message'] = 'ユーザーが既に存在します'
        else:
            id = str(uuid4())
            hashPASS = generate_password_hash(str(password))
            new_user = User(id=id, mail=str(mail),hashPASS=hashPASS,username=str(username))
            db.session.add(new_user)
            db.session.commit()
            result['message'] = 'successed'
            result['userid'] = User.search_by_mail(mail).id
        return result

    def delete(id):
        delete_user = User.search_by_id(id)
        db.session.delete(delete_user)
        db.session.commit()
        return

    def auth(mail, password):
        result = {}
        found_user = User.search_by_mail(mail)
        if found_user == None:
            result['message'] = 'ユーザーが存在しません'
        elif check_password_hash(found_user.hashPASS, str(password)) == False:
            result['message'] = 'PASSが誤っています'
        else:
            result['message'] = 'successed'
            result['userid'] = found_user.id
        return result
