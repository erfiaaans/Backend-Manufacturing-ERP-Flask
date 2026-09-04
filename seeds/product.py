from backend_manufacturing_erp_flask import  create_app
from backend_manufacturing_erp_flask.extensions import db
from backend_manufacturing_erp_flask.models.product import Product
def seed_products():
    app = create_app()
    products = [
        {
            "code": "PRD-001",
            "name": "Meja Kantor",
            "description": "Meja kantor berbahan kayu",
            "category": "Furniture",
            "unit": "pcs",
            "selling_price": 1250000,
        },
        {
            "code": "PRD-002",
            "name": "Kursi Kantor",
            "description": "Kursi kantor ergonomis",
            "category": "Furniture",
            "unit": "pcs",
            "selling_price": 850000,
        },
        {
            "code": "PRD-003",
            "name": "Lemari Arsip",
            "description": "Lemari arsip kayu",
            "category": "Furniture",
            "unit": "pcs",
            "selling_price": 2100000,
        },
        {
            "code": "PRD-004",
            "name": "Rak Buku",
            "description": "Rak buku kantor",
            "category": "Furniture",
            "unit": "pcs",
            "selling_price": 1750000,
        },
        {
            "code": "PRD-005",
            "name": "Meja Meeting",
            "description": "Meja meeting kapasitas 8 orang",
            "category": "Furniture",
            "unit": "pcs",
            "selling_price": 3500000,
        },
    ]
    with app.app_context():
        created_count = 0
        for data in products:
            if not Product.query.filter_by(code=data["code"]).first():
                db.session.add(Product(**data))
                created_count += 1
        db.session.commit()
        print(f"{created_count} product(s) created successfully.")
if __name__ == "__main__":
    seed_products()