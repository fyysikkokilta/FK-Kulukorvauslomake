from bottle import request, abort

class AuthorizationPlugin:
    def __init__(self, group):
        self._group = group
    def apply(self, callback, route):
        def wrapper(*args, **kwargs):
            if not request.user or self._group not in request.user['groups']:
                abort(401, 'Unauthorized.')
            return callback(*args, **kwargs)
        return wrapper
