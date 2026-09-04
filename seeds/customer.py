from backend_manufacturing_erp_flask import create_app
from backend_manufacturing_erp_flask.extensions import db
from backend_manufacturing_erp_flask.models.customer import Customer

def seed_customers():
    app = create_app()
    customers = [
        {
            "code": "CUS-001",
            "name": "PT Maju Jaya",
            "phone": "081234567811",
            "email": "purchasing@majujaya.com",
            "address": "Madiun, Jawa Timur",
        },
        {
            "code": "CUS-002",
            "name": "CV Sejahtera",
            "phone": "081234567812",
            "email": "admin@sejahtera.com",
            "address": "Ngawi, Jawa Timur",
        },
        {
            "code": "CUS-003",
            "name": "PT Nusantara Abadi",
            "phone": "081234567813",
            "email": "procurement@nusantara.com",
            "address": "Surakarta, Jawa Tengah",
        },
        {
            "code": "CUS-004",
            "name": "PT Sentosa Furniture",
            "phone": "081234567814",
            "email": "purchasing@sentosa.com",
            "address": "Malang, Jawa Timur",
        },
    ]
    with app.app_context():
        created_count = 0
        for data in customers:
            if not Customer.query.filter_by(code=data["code"]).first():
                db.session.add(Customer(**data))
                created_count +=1
        db.session.commit()
        print(f"{created_count} customer(s) created successfully.")
if __name__ == "__main__":
    seed_customers()