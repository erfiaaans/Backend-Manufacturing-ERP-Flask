from datetime import datetime
from ..extensions import db
class Supplier(db.Model):
    __tablename__ = "suppliers"
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
    phone = db.Column(
        db.String(30),
        nullable=True
    )
    email = db.Column(
        db.String(120),
        nullable=True
    )
    address=db.Column(
        db.Text,
        nullable=True
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
    