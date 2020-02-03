from marshmallow import fields, Schema, validates


class CategorySchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    parent = fields.Nested("self")
    is_root = fields.Boolean(default=False)
    subcategories = fields.List(fields.Nested("self"))


class ProductSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    price = fields.Integer(required=True)
    category = fields.Nested(CategorySchema)
    amount = fields.Integer(required=True)
    views = fields.Integer()