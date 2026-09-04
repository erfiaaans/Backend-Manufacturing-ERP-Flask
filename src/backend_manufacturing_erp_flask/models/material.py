from datetime import datetime
from ..extensions import db

class Material(db.Model):
    __tablename__ = "materials"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(
        db.String(30),
        unique=True,
        nullable=False
    )
    name = db.Column(
        db.String(150),
        nullable=False
    )
    category = db.Column(
        db.String(100),
        nullable=False
    )
    unit = db.Column(
        db.String(20),
        nullable=False
    )
    minimum_stock = db.Column(
        db.Numeric(15, 2),
        nullable=False,
        default=0
    )
    purchase_price = db.Column(
        db.Numeric(15, 2),
        nullable=False,
        default=0
    )
    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
    