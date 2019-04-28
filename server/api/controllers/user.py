
from api.middleware.cheack_auth import pwd_context, secret
from api.serializers.user import UserSchema
from api.models.user import User
from datetime import datetime, timedelta
from marshmallow import ValidationError
from peewee import IntegrityError
import jwt
import bottle

user_schema = UserSchema()

def userRegister(json_input):
    try:
        data, errors = user_schema.load(json_input)
        if errors:
            raise ValidationError(errors) 
    except ValidationError as err:
        return {
            'status': 0,
            'errors': err.messages,
        }
    
    try:
        User.get(User.username == json_input['username'])
    except User.DoesNotExist:
        pass
    else:
        return {
            'status': 0,
            'errors': 'The username is already register'
        }
    
    try:
        User.get(User.email == json_input['email'])
    except User.DoesNotExist:
        pass
    else:
        return {
                'status': 0,
                'errors': 'The email address is already register'
        }

    try:
        password_hash = pwd_context.hash(json_input['password'])
        json_input['password'] = password_hash
        user = User.create(**json_input)
    except IntegrityError:
        return {
            'status': 0,
            'errors': 'A database error has ocurred.'
        }
    else:
        data , errors = user_schema.dump(user)
        return {
            'status': 'ok',
            'data': data
        }

def userLogin(json_input):
    try:
        user = User.get(User.username == json_input['username'])
    except User.DoesNotExist:
        return {
            'status': 401,
            'errors': 'Username doesn\'t exist',
        }
    
    try:
        validated = pwd_context.verify(json_input['password'], user.password)
    except:
        return {
            'status': 401,
            'errors': 'Wrong password',
        }
    else:
        if validated:
            exp = datetime.utcnow() + timedelta(days=1)
            jwtoken = jwt.encode({'exp' : exp, 'userID' : user.id}, secret, algorithm='HS256').decode('utf-8')
            return {
                'status': 'ok',
                'jwtoken': jwtoken,
            }
        else:        
            return {
                'status': 401,
                'errors': 'Wrong password',
            }
