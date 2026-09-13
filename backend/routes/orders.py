import time
import json
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from extensions import db
from models.order import Order
from routes.admin import get_admin_or_error

orders_bp = Blueprint('orders', __name__)

REQUIRED_FIELDS = [
    'first_name', 'last_name', 'email', 'phone', 'address', 'city',
    'payment_method', 'items', 'subtotal', 'shipping_fee', 'total'
]


def generate_order_number():
    return 'FR' + format(int(time.time() * 1000), 'x').upper()


@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json or {}

    for field in REQUIRED_FIELDS:
        if data.get(field) in (None, '', []):
            return jsonify({'message': f'{field} is required'}), 400

    if not isinstance(data['items'], list) or len(data['items']) == 0:
        return jsonify({'message': 'Order must include at least one item'}), 400

    order = Order(
        order_number=generate_order_number(),
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone=data['phone'],
        address=data['address'],
        city=data['city'],
        payment_method=data['payment_method'],
        items=json.dumps(data['items']),
        subtotal=int(data['subtotal']),
        shipping_fee=int(data['shipping_fee']),
        total=int(data['total'])
    )

    db.session.add(order)
    db.session.commit()

    return jsonify(order.to_dict()), 201


@orders_bp.route('/admin/orders', methods=['GET'])
@jwt_required()
def list_orders():
    _, error = get_admin_or_error()
    if error:
        return error

    orders = Order.query.order_by(Order.created_at.desc()).all()
    return jsonify([o.to_dict() for o in orders])
