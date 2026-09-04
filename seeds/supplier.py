from backend_manufacturing_erp_flask import create_app
from backend_manufacturing_erp_flask.extensions import db
from backend_manufacturing_erp_flask.models.supplier import Supplier

def seed_suppliers():
    app = create_app()
    suppliers = [
        {
            "code": "SUP-001",
            "name": "PT Kayu Makmur",
            "phone": "081234567801",
            "email": "sales@kayumakmur.com",
            "address": "Madiun, Jawa Timur",
        },
        {
            "code": "SUP-002",
            "name": "CV Sumber Material",
            "phone": "081234567802",
            "email": "info@sumbermaterial.com",
            "address": "Ponorogo, Jawa Timur",
        },
        {
            "code": "SUP-003",
            "name": "PT Warna Abadi",
            "phone": "081234567803",
            "email": "sales@warnaabadi.com",
            "address": "Surabaya, Jawa Timur",
        },
        {
            "code": "SUP-004",
            "name": "CV Jaya Hardware",
            "phone": "081234567804",
            "email": "jaya@hardware.com",
            "address": "Kediri, Jawa Timur",
        },
    ]
    with app.app_context():
        created_count = 0
        for data in suppliers:
            if not Supplier.query.filter_by(code=data["code"]).first():
                db.session.add(Supplier(**data))
                created_count +=1
        db.session.commit()
        print(f"{created_count} supplier(s) created successfully.")
if __name__ == "__main__":
    seed_suppliers()
