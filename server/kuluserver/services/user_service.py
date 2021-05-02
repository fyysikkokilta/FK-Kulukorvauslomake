'''Module containing user service'''
import bcrypt
from bottle import response, abort
from pony import orm
import time
from kuluserver.models import Users  # pylint: disable=E0401
import jwt

def set_session_cookie(email):
    token = jwt.encode({
        'uid': email,
        'iss': 'fk-kulu',
        'iat': time.time(),
        'exp': time.time() + 3600,
    }, 'secret', algorithm='HS512')

    response.set_cookie(
        'session', token, httponly=True, max_age=3600, path='/')

class UserService:
    '''User service class that provides access User model'''
    @orm.db_session
    def get(self, email):
        '''Get single user by email'''
        return Users.get(email=email).dictify()

    @orm.db_session
    def getAll(self):
        '''Get all users'''
        return [u.dictify() for u in orm.select(u for u in Users)[:]]

    @orm.db_session
    def add(self, **kwargs):
        return Users.create(**kwargs)

    @orm.db_session
    def login(self, email, password):
        user = Users.get(email=email)

        if not user or not bcrypt.checkpw(password.encode(), user.password_hash):
            abort(401, 'Authentication failed')

        set_session_cookie(email)
        return user.dictify()

    @orm.db_session
    def register(self, email, password):
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return Users.create(email=email, password_hash=password_hash).dictify()
