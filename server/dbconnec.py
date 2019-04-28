
from peewee import SqliteDatabase, Model

DATABASE = 'notes.db'
database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    """ Base Model class for model definition
    """
    class Meta:
        database = database