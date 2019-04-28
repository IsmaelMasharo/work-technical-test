
from dbconnec import BaseModel
from peewee import CharField, DateTimeField

class User(BaseModel):
    username = CharField(max_length=40, unique=True)
    password = CharField()
    email = CharField(max_length=40, unique=True)

