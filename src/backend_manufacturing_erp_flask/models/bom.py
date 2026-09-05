from datetime import datetime

from backend_manufacturing_erp_flask.extensions import db


class BOM(db.Model):
    __tablename__ = "boms"

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    version = db.Column(db.String(20), nullable=False, default="1.0")

    is_active = db.Column(db.Boolean, default=True, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
