from uuid import uuid4
from typing import Self
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from models import (
    JWTPost,
    User,
    UserPost,
    UserPut
)
from extensions import db_orm

class UserHelper():

    def search_by_id(self: Self, id: str) -> User | None:
        return User.query.filter_by(id=id).one_or_none()
    
    def search_by_mail(self: Self, mail: str) -> User | None:
        return User.query.filter_by(mail=mail).one_or_none()

    def create(self: Self, data: UserPost) -> str:
        if self.search_by_mail(data.mail):
            return 'メールアドレスの使用者が既に存在します'
        else: 
            password_hash: str = generate_password_hash(data.password)
            new_user = User(
                id=str(uuid4()),
                mail=data.mail,
                password_hash=password_hash,
                name=data.name
            )
            db_orm.session.add(new_user)
            db_orm.session.commit()
            return '成功'

    def authenticate(self: Self, data: JWTPost) -> dict[str, str]:
        found_user: User | None = self.search_by_mail(data.mail)
        if found_user == None:
            return {'msg': 'メールアドレスが存在しません'}
        elif check_password_hash(found_user.password_hash, data.password) == False:
            return {'msg': 'パスワードが誤っています'}
        else:
            return {'msg': '成功', 'user_id': found_user.id}

    def delete(self: Self, id: str) -> None:
        delete_user: User | None = self.search_by_id(id)
        db_orm.session.delete(delete_user)
        db_orm.session.commit()

    def update_mail_address(self: Self, id: str, data: UserPut) -> dict[str, str | int]:
        if self.search_by_id(id).mail != data.current_val:
            return {'msg': '現メールアドレスが誤っています', 'status': 404}
        elif data.new_val != data.check_val:
            return {'msg': '新メールアドレスと確認用が一致しません', 'status': 422}
        elif self.search_by_mail(data.new_val) != None:
            return {'msg': '新メールアドレスの使用者が既に存在します', 'status': 409}
        else:
            self.search_by_id(id).mail = data.new_val
            db_orm.session.commit()
            return {'msg': '成功'}
    
    def update_password(self: Self, id: str, data: UserPut) -> dict[str, str | int]:
        if check_password_hash(self.search_by_id(id).password_hash, data.current_val) == False:
            return {'msg': '現パスワードが誤っています', 'status': 404}
        elif data.new_val != data.check_val:
            return {'msg': '新パスワードと確認用が一致しません', 'status': 422}
        else:
            self.search_by_id(id).password_hash = generate_password_hash(data.new_val)
            db_orm.session.commit()
            return {'msg': '成功'}

    def update_user_name(self: Self, id: str, data: UserPut) -> dict[str, str | int]:
        if self.search_by_id(id).name != data.current_val:
            return {'msg': '現ユーザーネームが誤っています', 'status': 404}
        elif data.new_val != data.check_val:
            return {'msg': '新ユーザーネームと確認用が一致しません', 'status': 422}
        else:
            self.search_by_id(id).name = data.new_val
            db_orm.session.commit()
            return {'msg': '成功'}
