from backend_manufacturing_erp_flask.extensions import db


class BOMItem(db.Model):
    __tablename__ = "bom_items"

    id = db.Column(db.Integer, primary_key=True)

    bom_id = db.Column(db.Integer, db.ForeignKey("boms.id"), nullable=False)

    material_id = db.Column(db.Integer, db.ForeignKey("materials.id"), nullable=False)

    quantity = db.Column(db.Numeric(15, 2), nullable=False)
