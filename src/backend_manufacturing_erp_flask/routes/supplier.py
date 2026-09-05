from flask import Blueprint, request
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from ..extensions import db
from ..models.supplier import Supplier
from ..schemas.supplier import supplier_schema, suppliers_schema

supplier_bp = Blueprint("supplier", __name__, url_prefix="/api/suppliers")


@supplier_bp.get("")
def list_suppliers():
    suppliers = Supplier.query.order_by(Supplier.id.asc()).all()
    return {"status": "success", "data": suppliers_schema.dump(suppliers)}, 200


@supplier_bp.get("/<int:supplier_id>")
def get_supplier(supplier_id):
    supplier = Supplier.query.get(supplier_id)
    if not supplier:
        return {"status": "error", "message": "Supplier not found"}, 404
    return {"status": "success", "data": supplier_schema.dump(supplier)}, 200


@supplier_bp.post("")
def create_supplier():
    json_data = request.get_json()
    if not json_data:
        return {"status": "error", "message": "Request body is required"}, 400

    # validasi sederhana code & name wajib
    if not json_data.get("code") or not json_data.get("name"):
        return {"status": "error", "message": "code and name are required"}, 400

    # cek duplikat code
    if Supplier.query.filter_by(code=json_data["code"]).first():
        return {"status": "error", "message": "Supplier code already exists"}, 409

    try:
        supplier = supplier_schema.load(json_data)
    except ValidationError as err:
        return {
            "status": "error",
            "message": "Validation error",
            "errors": err.messages,
        }, 400

    try:
        db.session.add(supplier)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {"status": "error", "message": "Supplier code already exists"}, 409

    return {
        "status": "success",
        "message": "Supplier created",
        "data": supplier_schema.dump(supplier),
    }, 201


@supplier_bp.put("/<int:supplier_id>")
def update_supplier(supplier_id):
    supplier = Supplier.query.get(supplier_id)
    if not supplier:
        return {"status": "error", "message": "Supplier not found"}, 404

    json_data = request.get_json()
    if not json_data:
        return {"status": "error", "message": "Request body is required"}, 400

    # cek duplikat code jika code diubah
    new_code = json_data.get("code")
    if new_code and new_code != supplier.code:
        if Supplier.query.filter_by(code=new_code).first():
            return {"status": "error", "message": "Supplier code already exists"}, 409

    try:
        supplier = supplier_schema.load(json_data, instance=supplier, partial=False)
    except ValidationError as err:
        return {
            "status": "error",
            "message": "Validation error",
            "errors": err.messages,
        }, 400

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {"status": "error", "message": "Supplier code already exists"}, 409

    return {
        "status": "success",
        "message": "Supplier updated",
        "data": supplier_schema.dump(supplier),
    }, 200


@supplier_bp.delete("/<int:supplier_id>")
def delete_supplier(supplier_id):
    supplier = Supplier.query.get(supplier_id)
    if not supplier:
        return {"status": "error", "message": "Supplier not found"}, 404

    db.session.delete(supplier)
    db.session.commit()
    return {"status": "success", "message": "Supplier deleted"}, 200
