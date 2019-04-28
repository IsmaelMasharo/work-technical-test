
from passlib.context import CryptContext
from bottle import request, abort
import jwt

secret = "SUPERSECRETO"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

class AuthorizationError(Exception):
    """ A base class for exceptions used by bottle. 
    """
    pass
 
def jwt_token_from_header():
    auth = request.headers.get('Authorization', None)
    if not auth:
        raise AuthorizationError({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'})
 
    parts = auth.split()
 
    if parts[0].lower() != 'bearer':
        raise AuthorizationError({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'})
    elif len(parts) == 1:
        raise AuthorizationError({'code': 'invalid_header', 'description': 'Token not found'})
    elif len(parts) > 2:
        raise AuthorizationError({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'})
 
    return parts[1]
 
def requiresAuth(f):
    """ Provides JWT based authentication for any decorated function 
        assuming credentials available in an "Authorization" header
    """
    def decorated(*args, **kwargs):

        try:
            token = jwt_token_from_header()
        except AuthorizationError:
            abort(400, 'no autorization')

        try:
            token_decoded = jwt.decode(token, secret)
            args+=(token_decoded,)
        except jwt.ExpiredSignature:
            abort(401, 'token is expired')
        except jwt.DecodeError:
            abort(401, 'Error decoding signature')
 
        return f(*args, **kwargs)
 
    return decorated
