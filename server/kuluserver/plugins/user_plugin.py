import bottle
import jwt

class UserPlugin:
    def __init__(self, user_service):
        self._user_service = user_service

    def apply(self, callback, route):
        def wrapper(*args, **kwargs):
            enc_session = bottle.request.cookies.get('session')
            if not enc_session:
                bottle.request.user = None
                return callback(*args, **kwargs)

            try:
                session = jwt.decode(enc_session, 'secret', algorithms=['HS512'])
                bottle.request.user = self._user_service.get(session['uid'])
            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                bottle.abort(401, 'Authentication failed.')
            return callback(*args, **kwargs)
        return wrapper
