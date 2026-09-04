from backend_manufacturing_erp_flask import create_app
from backend_manufacturing_erp_flask.extensions import db
from backend_manufacturing_erp_flask.models.material import Material


def seed_materials():
    app = create_app()
    materials = [
        {
            "code": "MAT-001",
            "name": "Kayu Jati",
            "category": "Kayu",
            "unit": "kg",
            "minimum_stock": 100,
            "purchase_price": 75000,
        },
        {
            "code": "MAT-002",
            "name": "Kayu Mahoni",
            "category": "Kayu",
            "unit": "kg",
            "minimum_stock": 100,
            "purchase_price": 55000,
        },
        {
            "code": "MAT-003",
            "name": "Papan MDF",
            "category": "Papan",
            "unit": "lembar",
            "minimum_stock": 50,
            "purchase_price": 120000,
        },
        {
            "code": "MAT-004",
            "name": "Cat Kayu",
            "category": "Finishing",
            "unit": "liter",
            "minimum_stock": 20,
            "purchase_price": 85000,
        },
        {
            "code": "MAT-005",
            "name": "Lem Kayu",
            "category": "Finishing",
            "unit": "kg",
            "minimum_stock": 20,
            "purchase_price": 45000,
        },
        {
            "code": "MAT-006",
            "name": "Baut",
            "category": "Hardware",
            "unit": "pcs",
            "minimum_stock": 500,
            "purchase_price": 500,
        },
        {
            "code": "MAT-007",
            "name": "Engsel",
            "category": "Hardware",
            "unit": "pcs",
            "minimum_stock": 100,
            "purchase_price": 7500,
        },
    ]
    with app.app_context():
        created_count = 0
        for data in materials:
            if not Material.query.filter_by(code=data["code"]).first():
                db.session.add(Material(**data))
                created_count += 1
        db.session.commit()
        print(f"{created_count} material(s) created successfully.")


if __name__ == "__main__":
    seed_materials()
