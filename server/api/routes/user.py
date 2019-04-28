
from api.middleware.corsUtil import enable_cors 
import api.controllers.user as userController
from bottle import request, Bottle

userApp = Bottle()

@userApp.route('/signup', method=['OPTIONS', 'POST'])
@enable_cors
def signUp():
    """ Route for sign up.
        Returns basic registration info.
    """

    status = userController.userRegister(request.json)
    return status

@userApp.route('/login', method=['OPTIONS', 'POST'])
@enable_cors
def login():
    """ Route for login.
        Returns basic login info and JWT.
    """

    status = userController.userLogin(request.json)
    return status