from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from ..extensions import db
from ..models.user import User
auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)

@auth_bp.post("/register")
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    
    if not username or not email or not password:
        return{
            "message": "Username, email, and password are required"
        }, 400
    existing_user = User.query.filter(
        (User.username == username) |
        (User.email == email)
    ).first()
    if existing_user:
        return{
            "message": "Username or email already exists"
        }, 409
    user = User(
        username=username,
        email=email
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return{
        "message": "User registered succesfully"
    }, 201
@auth_bp.post("/login")
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    
    user = User.query.filter_by(
        email=email
    ).first()
    if not user:
        return{
            "message": "Invalid crendetials"
        }, 401
    if not user.check_password(password):
        return{
            "message": "Invalid credentials"
        }, 401
    access_token = create_access_token(
        identity=str(user.id)
    )
    return{
        "access_token": access_token
    }