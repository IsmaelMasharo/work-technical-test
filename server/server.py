
from app import build_application
from dbconnec import database
from api.models.user import User
from api.models.notes import Note

def createOwnTables():
    """ Create tables if dont exist.
    """
    try:
        database.create_tables([User, Note])
    except:
        pass

if __name__ == '__main__':
    """ Main module.
    """
    
    createOwnTables()
    app = build_application()
    app.run(reloader=True, host='127.0.0.1', port=8000)