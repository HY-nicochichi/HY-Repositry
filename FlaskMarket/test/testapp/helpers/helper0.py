from flask import session

# Sessionモデルは、セッション管理ライブラリ(Beaker)内で定義されている

class SessionHelper():

    def log_in(user_id):
        session.clear()
        session.permanent = True
        session['user'] = user_id
        session['basket'] = {}

    def log_out():
        session.clear()
        session.permanent = True
