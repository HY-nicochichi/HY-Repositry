from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
from models import User
from extensions import db_orm

class UserHelper():

    def search_by_user_id(self, user_id):
        return User.query.filter_by(user_id=user_id).one_or_none()
    
    def search_by_mail(self, mail):
        return User.query.filter_by(mail=mail).one_or_none()

    def register(self, mail, password, username):
        if self.search_by_mail(mail):
            return 'メールアドレスの使用者が既に存在します'
        else:
            hashPASS = generate_password_hash(password)
            new_user = User(user_id=str(uuid4()), mail=mail, hashPASS=hashPASS, username=username)
            db_orm.session.add(new_user)
            db_orm.session.commit()
            return '成功'

    def authenticate(self, mail, password):
        found_user = self.search_by_mail(mail)
        if found_user == None:
            return {'msg': 'メールアドレスが存在しません'}
        elif check_password_hash(found_user.hashPASS, password) == False:
            return {'msg': 'パスワードが誤っています'}
        else:
            return {'msg': '成功', 'user_id': found_user.user_id}

    def update_mail(self, user_id, current_mail, new_mail, check_mail):
        if self.search_by_user_id(user_id).mail != current_mail:
            return '現メールアドレスが誤っています'
        elif new_mail != check_mail:
            return '新メールアドレスと確認用が一致しません'
        elif self.search_by_mail(new_mail) != None:
            return '新メールアドレスの使用者が既に存在します'
        else:
            self.search_by_user_id(user_id).mail = new_mail
            db_orm.session.commit()
            return '成功'

    def update_password(self, user_id, current_pass, new_pass, check_pass):
        if check_password_hash(self.search_by_user_id(user_id).hashPASS, current_pass) == False:
            return '現パスワードが誤っています'
        elif new_pass != check_pass:
            return '新パスワードと確認用が一致しません'
        else:
            self.search_by_user_id(user_id).hashPASS = generate_password_hash(new_pass)
            db_orm.session.commit()
            return '成功'

    def update_username(self, user_id, current_name, new_name, check_name):
        if self.search_by_user_id(user_id).username != current_name:
            return '現ユーザーネームが誤っています'
        elif new_name != check_name:
            return '新ユーザーネームと確認用が一致しません'
        else:
            self.search_by_user_id(user_id).username = new_name
            db_orm.session.commit()
            return '成功'

    def delete(self, user_id):
        db_orm.session.delete(self.search_by_user_id(user_id))
        db_orm.session.commit()
