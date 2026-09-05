from datetime import datetime

from backend_manufacturing_erp_flask.extensions import db


class Inventory(db.Model):
    __tablename__ = "inventories"

    id = db.Column(db.Integer, primary_key=True)

    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouses.id"), nullable=False)

    material_id = db.Column(db.Integer, db.ForeignKey("materials.id"), nullable=True)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=True)

    quantity = db.Column(db.Numeric(15, 2), nullable=False, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
