from flask import session
from sqlalchemy import text
from datetime import datetime
from extensions import db_orm, scheduler
from settings import cookie_life

# Sessionモデルは、セッション管理ライブラリ(Beaker)内で定義されている

class SessionHelper():

    @scheduler.task('interval', days=1)
    def del_old_sessions():
        try:
            create_limit = datetime.now() - cookie_life
            del_SQL = text('delete from sessions where created<:create_limit')
            with scheduler.app.app_context():
                db_orm.session.execute(del_SQL, {'create_limit': create_limit})
                db_orm.session.commit()
        except:
            pass

    def log_in(user_id):
        session_ID = str(session.id)
        del_SQL = text('delete from sessions where namespace=:session_ID')
        db_orm.session.execute(del_SQL, {'session_ID': session_ID})
        db_orm.session.commit()
        session.invalidate()
        session['user'] = user_id
        session['basket'] = {}

    def log_out():
        session_ID = str(session.id)
        del_SQL = text('delete from sessions where namespace=:session_ID')
        db_orm.session.execute(del_SQL, {'session_ID': session_ID})
        db_orm.session.commit()
        session.invalidate()
