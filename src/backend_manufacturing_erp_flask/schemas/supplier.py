from marshmallow import fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..extensions import db
from ..models.supplier import Supplier


class SupplierSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier
        sqla_session = db.session
        load_instance = True
        include_fk = True

    id = fields.Integer(dump_only=True)
    code = fields.String(required=True, validate=validate.Length(min=1, max=30))
    name = fields.String(required=True, validate=validate.Length(min=1, max=150))
    phone = fields.String(allow_none=True, validate=validate.Length(max=30))
    email = fields.Email(allow_none=True, validate=validate.Length(max=120))
    address = fields.String(allow_none=True)
    is_active = fields.Boolean(load_default=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)
