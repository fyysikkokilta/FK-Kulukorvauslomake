from bottle import request
import json
import kuluserver.plugins as plugins
from .controller import Controller

class UserController(Controller):
    def __init__(self, user_service):
        routes = [
            {
                'path': '/users',
                'callback': self.get_users,
                'apply': [
                    plugins.AuthorizationPlugin('admin'),
                ],
            },
            {
                'path': '/users/login',
                'method': ['POST'],
                'callback': self.login,
            },
            {
                'path': '/users/register',
                'method': ['POST'],
                'callback': self.register,
                'apply': [
                    plugins.AuthorizationPlugin('admin'),
                ],
            },
            {
                'path': '/users/me',
                'callback': self.me,
                'apply': [
                    plugins.AuthorizationPlugin('user'),
                ]
            },
        ]

        self._user_service = user_service
        super(UserController, self).__init__(routes)

    def get_users(self):
        return json.dumps(self._user_service.getAll())

    def login(self):
        email = request.json.get('email')
        password = request.json.get('password')
        return self._user_service.login(email, password)

    def register(self):
        email = request.json.get('email')
        password = request.json.get('password')
        return self._user_service.register(email, password)

    def me(self):
        return json.dumps(request.user)
