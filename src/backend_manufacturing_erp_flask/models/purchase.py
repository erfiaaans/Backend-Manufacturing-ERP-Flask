from datetime import datetime

from backend_manufacturing_erp_flask.extensions import db


class Purchase(db.Model):
    __tablename__ = "purchases"

    id = db.Column(db.Integer, primary_key=True)

    purchase_number = db.Column(db.String(50), unique=True, nullable=False)

    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"), nullable=False)

    status = db.Column(db.String(30), nullable=False, default="draft")

    order_date = db.Column(db.Date, nullable=False)

    total_amount = db.Column(db.Numeric(15, 2), nullable=False, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
