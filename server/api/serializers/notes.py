
from marshmallow import Schema, fields, validate, pre_load, post_dump, post_load, ValidationError
from api.serializers.user import UserSchema
from api.models.notes import Note

class NoteSchema(Schema):

    id = fields.Int(dump_only=True)
    user = fields.Nested(UserSchema, exclude=('password'), dump_only=True)
    content = fields.Str(required=True)
    creation_date = fields.DateTime(dump_only=True)

    # an envelope to responses
    @post_dump(pass_many=True)
    def wrap(self, data, many):
        key = 'notes' if many else 'note'
        return {
            key: data,
        }

    # create a new note from validated data
    @post_load
    def make_object(self, data):
        if not data:
            return None
        return Note(
            content=data['content'],
            creation_date=dt.datetime.today(),
        )
