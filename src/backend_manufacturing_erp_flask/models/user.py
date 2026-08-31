from datetime import datetime
from ..extensions import db 
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False 
    )
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False 
    )
    password_hash = db.Column(
        db.String(255),
        nullable=False 
    )
    role = db.Column(
        db.String(30),
        nullable=False,
        default="staff"
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
    