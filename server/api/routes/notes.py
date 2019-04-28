
import api.controllers.notes as noteController
from bottle import request, Bottle
from api.middleware.cheack_auth import requiresAuth, jwt_token_from_header
from api.middleware.corsUtil import enable_cors 

noteApp = Bottle()

@noteApp.route('/', method=['OPTIONS', 'GET'])
@enable_cors
@requiresAuth
def getAllNotes(*args):
    """ Route for getting all notes of a specific user.
        Require authentication
    """
    userID = args[0]["userID"]
    notes = noteController.allNotes(userID)
    return notes


@noteApp.route('/<noteID>', method=['OPTIONS', 'GET'])
@enable_cors
@requiresAuth
def getNoteByID(*args, noteID):
    """ Route for getting a single note of a specific user.
        Require authentication
    """

    userID = args[0]["userID"]
    note = noteController.singleNote(noteID, userID)
    return note


@noteApp.route('/', method=['OPTIONS', 'POST'])
@enable_cors
@requiresAuth
def postNote(*args):
    """ Route for posting a single note of a specific user.
        Require authentication
    """

    userID = args[0]["userID"]
    note = noteController.saveNote(request, userID)
    return note
