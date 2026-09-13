import json
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from extensions import db
from models.product import Product
from routes.admin import get_admin_or_error

products_bp = Blueprint('products', __name__)

REQUIRED_FIELDS = ['name', 'category', 'type', 'subtype', 'price', 'sizes']
VALID_CATEGORIES = {'man', 'woman'}
VALID_TAGS = {'New', 'Sale'}
SUBTYPES_BY_TYPE = {
    'clothing': {'tshirt', 'jacket', 'denim'},
    'accessories': {'glasses', 'hats', 'bags'}
}
MIN_IMAGES = 3


def validate_sizes(sizes):
    if not isinstance(sizes, list) or len(sizes) == 0:
        return False
    for entry in sizes:
        if not isinstance(entry, dict):
            return False
        if not entry.get('size') or not isinstance(entry.get('size'), str):
            return False
        if not isinstance(entry.get('available'), bool):
            return False
    return True


def validate_images(images):
    if images is None:
        return True  # allowed to be empty -> backend generates placeholders
    if not isinstance(images, list):
        return False
    return all(isinstance(url, str) and url.strip() for url in images)


def validate_product_payload(data):
    for field in REQUIRED_FIELDS:
        if data.get(field) in (None, '', []):
            return f'{field} is required'

    if data['category'] not in VALID_CATEGORIES:
        return 'Invalid category'

    if data['type'] not in SUBTYPES_BY_TYPE:
        return 'Invalid type'

    if data['subtype'] not in SUBTYPES_BY_TYPE[data['type']]:
        return 'Subtype does not match the selected type'

    if not isinstance(data['price'], (int, float)) or data['price'] <= 0:
        return 'Price must be a positive number'

    if data.get('salePrice') not in (None, '') and (
        not isinstance(data['salePrice'], (int, float)) or data['salePrice'] <= 0
    ):
        return 'Sale price must be a positive number'

    if data.get('tag') not in (None, '', *VALID_TAGS):
        return 'Invalid tag'

    if not validate_sizes(data['sizes']):
        return 'Sizes must each have a size label and an availability flag'

    if not validate_images(data.get('images')):
        return 'Images must be a list of non-empty URLs'

    images = [url.strip() for url in (data.get('images') or [])]
    if images and len(images) < MIN_IMAGES:
        return f'Provide at least {MIN_IMAGES} images, or leave the field empty for placeholders'

    return None


def resolve_images(data):
    images = [url.strip() for url in (data.get('images') or []) if url.strip()]
    if images:
        return images

    seed = data['name'].strip().lower().replace(' ', '-')
    return [f'https://picsum.photos/seed/{seed}-{n}/700/900' for n in range(1, MIN_IMAGES + 1)]


@products_bp.route('/products', methods=['GET'])
def list_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])


@products_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify(product.to_dict())


@products_bp.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    _, error = get_admin_or_error()
    if error:
        return error

    data = request.json or {}
    validation_error = validate_product_payload(data)
    if validation_error:
        return jsonify({'message': validation_error}), 400

    product = Product(
        name=data['name'],
        category=data['category'],
        type=data['type'],
        subtype=data['subtype'],
        price=int(data['price']),
        sale_price=int(data['salePrice']) if data.get('salePrice') else None,
        tag=data.get('tag') or None,
        images=json.dumps(resolve_images(data)),
        sizes=json.dumps(data['sizes'])
    )

    db.session.add(product)
    db.session.commit()

    return jsonify(product.to_dict()), 201


@products_bp.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    _, error = get_admin_or_error()
    if error:
        return error

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    data = request.json or {}
    validation_error = validate_product_payload(data)
    if validation_error:
        return jsonify({'message': validation_error}), 400

    product.name = data['name']
    product.category = data['category']
    product.type = data['type']
    product.subtype = data['subtype']
    product.price = int(data['price'])
    product.sale_price = int(data['salePrice']) if data.get('salePrice') else None
    product.tag = data.get('tag') or None
    product.images = json.dumps(resolve_images(data))
    product.sizes = json.dumps(data['sizes'])

    db.session.commit()

    return jsonify(product.to_dict())


@products_bp.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    _, error = get_admin_or_error()
    if error:
        return error

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted'})
