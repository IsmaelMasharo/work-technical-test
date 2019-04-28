
from dbconnec import BaseModel
from peewee import ForeignKeyField, TextField, DateTimeField
from api.models.user import User

class Note(BaseModel):
    user = ForeignKeyField(User)
    content = TextField()
    creation_date = DateTimeField()