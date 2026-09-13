import json
from extensions import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(20), nullable=False)  # man | woman
    type = db.Column(db.String(20), nullable=False)  # clothing | accessories
    subtype = db.Column(db.String(20), nullable=False)  # tshirt | jacket | denim | glasses | hats | bags
    price = db.Column(db.Integer, nullable=False)  # RSD
    sale_price = db.Column(db.Integer)
    tag = db.Column(db.String(20))
    images = db.Column(db.Text, nullable=False)  # JSON array of image URLs, at least 3
    sizes = db.Column(db.Text, nullable=False)  # JSON array of {size, available}

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'type': self.type,
            'subtype': self.subtype,
            'price': self.price,
            'salePrice': self.sale_price,
            'tag': self.tag,
            'images': json.loads(self.images) if self.images else [],
            'sizes': json.loads(self.sizes) if self.sizes else []
        }
