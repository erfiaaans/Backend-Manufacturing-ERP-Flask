from backend_manufacturing_erp_flask import create_app
from backend_manufacturing_erp_flask.extensions import db
from backend_manufacturing_erp_flask.models.warehouse import Warehouse

def seed_warehouses():
    app = create_app()
    warehouses = [
        {
            "code": "WH-001",
            "name": "Gudang Bahan Baku",
            "location": "Area Produksi A",
        },
        {
            "code": "WH-002",
            "name": "Gudang Produk Jadi",
            "location": "Area Produksi B",
        },
        {
            "code": "WH-003",
            "name": "Gudang Utama",
            "location": "Gedung Utama",
        },
    ]
    with app.app_context():
        created_count = 0
        for data in warehouses:
            if not Warehouse.query.filter_by(code=data["code"]).first():
                db.session.add(Warehouse(**data))
                created_count += 1
        db.session.commit()
        print(f"{created_count} warehouse(s) created successfully.")
if __name__ == "__main__":
    seed_warehouses()
        