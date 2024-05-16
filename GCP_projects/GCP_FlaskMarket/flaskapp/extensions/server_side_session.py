from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware
from datetime import timedelta

class ServerSessionInterface(SessionInterface):

    def open_session(self, app, request):
        return request.environ.get('beaker.session')
        
    def save_session(self, app, session, response):
        session.save()

class ServerSession():
    
    def init_app(self, app):
        self.app = app
        self._session_conf = app.config.get('SERVER_SESSION', {})
        if 'session.key' not in self._session_conf:
            self._session_conf['session.key'] = 'session_id'
        if 'session.cookie_expires' not in self._session_conf:
            self._session_conf['session.cookie_expires'] = timedelta(days=7.0)
        if 'session.secret' not in self._session_conf:
            self._session_conf['session.secret'] = 'Session_Secret_Key'
        if 'session.httponly' not in self._session_conf:
            self._session_conf['session.httponly'] = True
        if 'session.auto' not in self._session_conf:
            self._session_conf['session.auto'] = True,
        if 'session.type' not in self._session_conf:
            self._session_conf['session.type'] = 'file'
            self._session_conf['session.data_dir'] = './server_session/data_dir'
            self._session_conf['session.lock_dir'] = './server_session/lock_dir'
        if self._session_conf['session.type'] == 'ext:database':
            if 'session.table_name' not in self._session_conf:
                self._session_conf['session.table_name'] = 'sessions'
        app.wsgi_app = SessionMiddleware(app.wsgi_app, self._session_conf)
        app.session_interface = ServerSessionInterface()
