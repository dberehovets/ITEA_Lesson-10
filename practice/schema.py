from marshmallow import fields, Schema, validates


class TagSchema(Schema):
    title = fields.String(required=True)


class AuthorSchema(Schema):
    name = fields.String(required=True)
    surname = fields.String(required=True)


class PostSchema(Schema):
    title = fields.String(required=True)
    content = fields.String()
    publication_date = fields.DateTime()
    author = fields.Nested(AuthorSchema, dump_only=True)
    views_amount = fields.Integer()
    tag = fields.Nested(TagSchema, dump_only=True)