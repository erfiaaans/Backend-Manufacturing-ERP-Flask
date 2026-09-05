from backend_manufacturing_erp_flask.extensions import db


class PurchaseItem(db.Model):
    __tablename__ = "purchase_items"

    id = db.Column(db.Integer, primary_key=True)

    purchase_id = db.Column(db.Integer, db.ForeignKey("purchases.id"), nullable=False)

    material_id = db.Column(db.Integer, db.ForeignKey("materials.id"), nullable=False)

    quantity = db.Column(db.Numeric(15, 2), nullable=False)

    unit_price = db.Column(db.Numeric(15, 2), nullable=False)

    subtotal = db.Column(db.Numeric(15, 2), nullable=False)
