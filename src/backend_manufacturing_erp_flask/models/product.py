from datetime import datetime
from ..extensions import db
class Product (db.Model):
    __tablename__ = "products"
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
    description = db.Column(
        db.Text,
        nullable=True
    )
    category = db.Column(
        db.String(100),
        nullable=False
    )
    unit =db.Column(
        db.String(20),
        nullable=False
    )
    selling_price = db.Column(
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