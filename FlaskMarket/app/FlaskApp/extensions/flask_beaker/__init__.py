'''
    flaskext.beaker
    ---------------
    
    A Flask extension providing beaker session interface.
    
    :copyright: (c) 2012 by Syrus Akbary.
    :license: MIT, see LICENSE for more details.
'''

__version__ = '0.2.0' # 一部コードを改造いたしました。

from flask.sessions import SessionInterface

try:
    from beaker.middleware import SessionMiddleware
except ImportError as e:
    print('Beaker package is required to use Flask-Beaker')
    raise e

class BeakerSessionInterface(SessionInterface):

    def open_session(self, app, request):
        return request.environ['beaker.session']
        
    def save_session(self, app, session, response):
        session.save()

class BeakerSession(object):
    
    def init_app(self, app):  # app: Flask
        self.app = app
        self._session_conf = app.config['BEAKER_SESSION']
        app.wsgi_app = SessionMiddleware(app.wsgi_app, self._session_conf)
        app.session_interface = BeakerSessionInterface()
