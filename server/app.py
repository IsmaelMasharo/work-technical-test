
from api.routes.notes import noteApp
from api.routes.user import userApp   
from bottle import Bottle

def build_application():
    """ Creates the main app to be instantiated for the server.
    """    
    # app definition
    root_app = Bottle()

    # routes
    root_app.mount('/notes', noteApp)
    root_app.mount('/user', userApp)
    
    return root_app
