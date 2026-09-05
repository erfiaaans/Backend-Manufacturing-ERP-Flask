from backend_manufacturing_erp_flask.extensions import db


class SalesItem(db.Model):
    __tablename__ = "sales_items"

    id = db.Column(db.Integer, primary_key=True)

    sales_id = db.Column(db.Integer, db.ForeignKey("sales.id"), nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    quantity = db.Column(db.Numeric(15, 2), nullable=False)

    unit_price = db.Column(db.Numeric(15, 2), nullable=False)

    subtotal = db.Column(db.Numeric(15, 2), nullable=False)
