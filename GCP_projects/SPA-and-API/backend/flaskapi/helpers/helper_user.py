from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
from models import User
from extensions import db_orm

class UserHelper():

    def search_by_id(user_id):
        found_user = User.query.filter_by(user_id=str(user_id)).one_or_none()
        return found_user
    
    def search_by_mail(mail):
        found_user = User.query.filter_by(mail=str(mail)).one_or_none()
        return found_user

    def register(mail, password, username):
        if UserHelper.search_by_mail(mail):
            result = {'message': 'メールアドレスの使用者が既に存在します'}
        else:
            user_id = str(uuid4())
            hashPASS = generate_password_hash(str(password))
            new_user = User(user_id=user_id, mail=str(mail), hashPASS=hashPASS, username=str(username))
            db_orm.session.add(new_user)
            db_orm.session.commit()
            result = {'message': '成功'}
        return result

    def auth(mail, password):
        found_user = UserHelper.search_by_mail(mail)
        if found_user == None:
            result = {'message': 'メールアドレスが存在しません'}
        elif check_password_hash(found_user.hashPASS, str(password)) == False:
            result = {'message': 'パスワードが誤っています'}
        else:
            result = {'message': '成功', 'user_id': found_user.user_id}
        return result

    def delete(user_id):
        delete_user = UserHelper.search_by_id(user_id)
        db_orm.session.delete(delete_user)
        db_orm.session.commit()

    def update_mail(user_id, current_mail, new_mail, check_mail):
        if UserHelper.search_by_id(user_id).mail != current_mail:
            result = '現メールアドレスが誤っています'
        elif new_mail != check_mail:
            result = '新メールアドレスと確認用が一致しません'
        elif UserHelper.search_by_mail(new_mail) != None:
            result = '新メールアドレスの使用者が既に存在します'
        else:
            UserHelper.search_by_id(user_id).mail = new_mail
            db_orm.session.commit()
            result = '成功'   
        return result
    
    def update_password(user_id, current_pass, new_pass, check_pass):
        if check_password_hash(UserHelper.search_by_id(user_id).hashPASS, current_pass) == False:
            result = '現パスワードが誤っています'
        elif new_pass != check_pass:
            result = '新パスワードと確認用が一致しません'
        else:
            UserHelper.search_by_id(user_id).hashPASS = generate_password_hash(new_pass)
            db_orm.session.commit()
            result = '成功'
        return result

    def update_username(user_id, current_name, new_name, check_name):
        if UserHelper.search_by_id(user_id).username != current_name:
            result = '現ユーザーネームが誤っています'
        elif new_name != check_name:
            result = '新ユーザーネームと確認用が一致しません'
        else:
            UserHelper.search_by_id(user_id).username = new_name
            db_orm.session.commit()
            result = '成功'
        return result
