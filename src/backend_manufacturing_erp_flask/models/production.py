from datetime import datetime

from backend_manufacturing_erp_flask.extensions import db


class Production(db.Model):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)

    production_number = db.Column(db.String(50), unique=True, nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouses.id"), nullable=False)

    quantity = db.Column(db.Numeric(15, 2), nullable=False)

    status = db.Column(db.String(30), nullable=False, default="planned")

    planned_date = db.Column(db.Date, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
