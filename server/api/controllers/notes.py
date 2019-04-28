
from api.serializers.notes import NoteSchema
from api.models.notes import Note
from api.models.user import User
from datetime import datetime
from peewee import IntegrityError

def allNotes(userID):
    try:
        notes = Note.select().where(Note.user == userID)
    except Note.DoesNotExist:
        return {
            'status': 'ok',
            'data': None
        }
    
    try:
        notes_schema = NoteSchema(many=True)
        result = notes_schema.dump(list(notes))
    except:
        notes_schema = NoteSchema()
        result = notes_schema.dump(notes)
    
    return {
            'status': 'ok',
            'data': result.data
    }


def singleNote(noteID, userID):
    try:
        note = Note.get(Note.id == int(noteID), Note.user == userID)
    except Note.DoesNotExist:
        return {
            'status': 'ok',
            'data': None
        }
    else:
        notes_schema = NoteSchema()
        result = notes_schema.dump(note)
        return {
            'status': 'ok',
            'data': result.data
        }

def saveNote(request, userID):
    try:
        note = Note.create(**request.json, creation_date = datetime.today(), user = userID)
    except IntegrityError:
        return {
            'status': 0,
            'errors': 'A database error has ocurred. Sorry.'
        }
    else:
        notes_schema = NoteSchema()
        data , errors = notes_schema.dump(note)
        return {
            'status': 'ok',
            'data': data
        }