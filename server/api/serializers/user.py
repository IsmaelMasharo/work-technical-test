
from marshmallow import Schema, fields, validate, pre_load, post_dump, post_load, ValidationError

class UserSchema(Schema):
    id = fields.Int(dump_only=True)

    email = fields.Str(
        required=True,
        validate=validate.Email(error='Not a valid email address'),
    )

    password = fields.Str(
        required=True,
        validate=[validate.Length(min=6, max=36)],
        load_only=True,
    )

    username = fields.Str(
        required=True,
        validate=[validate.Length(min=6, max=36)],
        load_only=True,
    )


    # Clean up data
    @pre_load
    def process_input(self, data):
        data['email'] = data['email'].lower().strip()
        return data

    # an envelope to responses
    @post_dump(pass_many=True)
    def wrap(self, data, many):
        key = 'users' if many else 'user'
        if many:
            return {
                key: data,
            }
        else:
            return data

