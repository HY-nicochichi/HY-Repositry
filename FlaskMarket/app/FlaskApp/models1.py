from werkzeug.security import generate_password_hash, check_password_hash
from orm import db, BaseModel

class User(BaseModel):

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    mail = db.Column(db.String(255), unique=True)
    hashPASS = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)

    def search_by_id(id):
        found_user = User.query.filter_by(id=id).first()
        return found_user
    
    def search_by_mail(mail):
        found_user = User.query.filter_by(mail=mail).first()
        return found_user

    def register(mail, password, username):
        result = {}
        if User.search_by_mail(mail) != None:
            result['message'] = 'ユーザーが既に存在します'
        else:
            hashPASS = generate_password_hash(password)
            new_user = User(mail=mail,hashPASS=hashPASS,username=username)
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
        elif check_password_hash(found_user.hashPASS, password) == False:
            result['message'] = 'PASSが誤っています'
        else:
            result['message'] = 'successed'
            result['userid'] = found_user.id
        return result
