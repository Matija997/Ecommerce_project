from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db, bcrypt
from models.user import User
from validators import validate_email_format, validate_password_strength, validate_phone_format

admin_bp = Blueprint('admin', __name__)
VALID_ROLES = {'user', 'editor', 'admin'}
STAFF_ROLES = {'editor', 'admin'}


def get_admin_or_error():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return None, (jsonify({"message": "User not found"}), 404)

    if user.role != "admin":
        return None, (jsonify({"message": "Forbidden"}), 403)

    return user, None


def get_staff_or_error():
    """Admins and editors both pass; editors just can't touch user management."""
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return None, (jsonify({"message": "User not found"}), 404)

    if user.role not in STAFF_ROLES:
        return None, (jsonify({"message": "Forbidden"}), 403)

    return user, None


@admin_bp.route('/admin/check', methods=['GET'])
@jwt_required()
def admin_check():
    user, error = get_admin_or_error()
    if error:
        return error

    return jsonify({
        "message": "Welcome admin",
        "email": user.email
    })


@admin_bp.route('/admin/users', methods=['GET'])
@jwt_required()
def list_users():
    _, error = get_admin_or_error()
    if error:
        return error

    users = User.query.order_by(User.id).all()
    return jsonify([u.to_dict() for u in users])


@admin_bp.route('/admin/users', methods=['POST'])
@jwt_required()
def create_user():
    _, error = get_admin_or_error()
    if error:
        return error

    data = request.json or {}

    required_fields = ['first_name', 'last_name', 'email', 'password',
                        'phone', 'address', 'city']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'message': f'{field} is required'}), 400

    if not validate_email_format(data['email']):
        return jsonify({'message': 'Invalid email'}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400

    if not validate_password_strength(data['password']):
        return jsonify({'message': 'Weak password'}), 400

    if not validate_phone_format(data['phone']):
        return jsonify({'message': 'Invalid phone'}), 400

    role = data.get('role', 'user')
    if role not in VALID_ROLES:
        return jsonify({'message': 'Invalid role'}), 400

    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=bcrypt.generate_password_hash(data['password']).decode('utf-8'),
        phone=data['phone'],
        address=data['address'],
        city=data['city'],
        role=role
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201


@admin_bp.route('/admin/users/<int:user_id>/role', methods=['PUT'])
@jwt_required()
def update_user_role(user_id):
    admin_user, error = get_admin_or_error()
    if error:
        return error

    target = User.query.get(user_id)
    if not target:
        return jsonify({"message": "User not found"}), 404

    role = (request.json or {}).get('role')
    if role not in VALID_ROLES:
        return jsonify({"message": "Invalid role"}), 400

    if target.id == admin_user.id and role != 'admin':
        return jsonify({"message": "You cannot remove your own admin access"}), 400

    target.role = role
    db.session.commit()

    return jsonify(target.to_dict())


@admin_bp.route('/admin/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    admin_user, error = get_admin_or_error()
    if error:
        return error

    if user_id == admin_user.id:
        return jsonify({"message": "You cannot delete your own account"}), 400

    target = User.query.get(user_id)
    if not target:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(target)
    db.session.commit()

    return jsonify({"message": "User deleted"})
