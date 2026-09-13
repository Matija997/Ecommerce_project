import json
from datetime import datetime
from extensions import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    payment_method = db.Column(db.String(20), nullable=False)
    items = db.Column(db.Text, nullable=False)  # JSON array of {product_id, name, image, size, qty, price}
    subtotal = db.Column(db.Integer, nullable=False)
    shipping_fee = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'order_number': self.order_number,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'city': self.city,
            'payment_method': self.payment_method,
            'items': json.loads(self.items) if self.items else [],
            'subtotal': self.subtotal,
            'shipping_fee': self.shipping_fee,
            'total': self.total,
            'created_at': self.created_at.isoformat()
        }
