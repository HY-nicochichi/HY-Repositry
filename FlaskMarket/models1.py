from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
from extensions import db_orm, BaseModel

class User(BaseModel):

    __tablename__ = 'users'

    id = db_orm.Column(db_orm.String(255), primary_key=True, nullable=False)
    mail = db_orm.Column(db_orm.String(255), unique=True, nullable=False)
    hashPASS = db_orm.Column(db_orm.String(255), nullable=False)
    username = db_orm.Column(db_orm.String(255), nullable=False)

    def search_by_id(id):
        found_user = User.query.filter_by(id=str(id)).first()
        return found_user
    
    def search_by_mail(mail):
        found_user = User.query.filter_by(mail=str(mail)).first()
        return found_user

    def register(mail, password, username):
        result = {}
        if User.search_by_mail(mail) != None:
            result['message'] = 'メールアドレスの使用者が既に存在します'
        else:
            id = str(uuid4())
            hashPASS = generate_password_hash(str(password))
            new_user = User(id=id, mail=str(mail), hashPASS=hashPASS, username=str(username))
            db_orm.session.add(new_user)
            db_orm.session.commit()
            result['message'] = 'successed'
            result['userid'] = User.search_by_mail(mail).id
        return result

    def delete(id):
        delete_user = User.search_by_id(id)
        db_orm.session.delete(delete_user)
        db_orm.session.commit()
        return

    def auth(mail, password):
        result = {}
        found_user = User.search_by_mail(mail)
        if found_user == None:
            result['message'] = 'ユーザーが存在しません'
        elif check_password_hash(found_user.hashPASS, str(password)) == False:
            result['message'] = 'パスワードが誤っています'
        else:
            result['message'] = 'successed'
            result['userid'] = found_user.id
        return result

    def update_mail(id, current_mail, new_mail, check_mail):
        if User.search_by_id(id).mail != current_mail:
            result = '現メールアドレスが誤っています'
        elif new_mail != check_mail:
            result = '新メールアドレスと確認用が一致しません'
        elif User.search_by_mail(new_mail) != None:
            result = '新メールアドレスの使用者が既に存在します'
        else:
            User.search_by_id(id).mail = new_mail
            db_orm.session.commit()
            result = 'success'   
        return result
    
    def update_password(id, current_pass, new_pass, check_pass):
        if check_password_hash(User.search_by_id(id).hashPASS, current_pass) == False:
            result = '現パスワードが誤っています'
        elif new_pass != check_pass:
            result = '新パスワードと確認用が一致しません'
        else:
            User.search_by_id(id).hashPASS = generate_password_hash(new_pass)
            db_orm.session.commit()
            result = 'success'
        return result

    def update_username(id, current_name, new_name, check_name):
        if User.search_by_id(id).username != current_name:
            result = '現ユーザーネームが誤っています'
        elif new_name != check_name:
            result = '新ユーザーネームと確認用が一致しません'
        else:
            User.search_by_id(id).username = new_name
            db_orm.session.commit()
            result = 'success'
        return result
