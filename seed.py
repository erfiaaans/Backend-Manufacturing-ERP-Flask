from backend_manufacturing_erp_flask import create_app
from seeds.customer import seed_customers
from seeds.material import seed_materials
from seeds.product import seed_products
from seeds.supplier import seed_suppliers
from seeds.users import seed_users
from seeds.warehouse import seed_warehouses


def seed():
    app = create_app()
    with app.app_context():
        seed_users()
        seed_products()
        seed_materials()
        seed_suppliers()
        seed_customers()
        seed_warehouses()


if __name__ == "__main__":
    seed()
