from marshmallow import fields as models, Schema


class DummySchema(Schema):
    id = models.Integer(required=True)
