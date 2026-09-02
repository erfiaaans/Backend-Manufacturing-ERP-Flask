from backend_manufacturing_erp_flask import create_app
from backend_manufacturing_erp_flask.extensions import db
from backend_manufacturing_erp_flask.models.user import User

def seed_users():
    app = create_app()
    with app.app_context():
        users =[
            {
                "username": "admin",
                "email": "admin@erp.com",
                "password": "admin123",
                "role": "admin",
            },
            {
                "username": "manager",
                "email": "manager@erp.com",
                "password": "manager123",
                "role": "manager",
            },
            {
                "username": "warehouse",
                "email": "warehouse@erp.com",
                "password": "warehouse123",
                "role": "warehouse",
            },
            {
                "username": "purchasing",
                "email": "purchasing@erp.com",
                "password": "purchasing123",
                "role": "purchasing",
            },
            {
                "username": "production",
                "email": "production@erp.com",
                "password": "production123",
                "role": "production",
            },
            {
                "username": "sales",
                "email": "sales@erp.com",
                "password": "sales123",
                "role": "sales",
            },
            {
                "username": "staff",
                "email": "staff@erp.com",
                "password": "staff123",
                "role": "staff",
            },   
        ]
        created_count = 0
        for data in users:
            existing_user = User.query.filter_by(
                email=data["email"]
            ).first()
            if existing_user:
                print(
                    f"User {data['username']} already exists. Skipped."
                )
                continue
            user = User(
                username=data["username"],
                email=data["email"],
                role=data["role"],
                is_active=True,
            )
            user.set_password(data["password"])
            db.session.add(user)
            created_count +=1
        db.session.commit()
        print(f"\n{created_count} user(s) created successfully.")
if __name__ == "__main__":
    seed_users()