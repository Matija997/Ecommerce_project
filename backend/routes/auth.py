from flask import Blueprint, request, jsonify
from extensions import db, bcrypt
from flask_jwt_extended import create_access_token
from models.user import User
import re

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json

    # Required fields
    required_fields = ['first_name', 'last_name', 'email', 'password',
                       'address', 'city']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'message': f'{field} is required'}), 400

    # Email format
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', data['email']):
        return jsonify({'message': 'Invalid email'}), 400

    # Email exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400

    # Password validation
    password = data['password']
    if (len(password) < 8 or
        not re.search(r'[A-Z]', password) or
        not re.search(r'[a-z]', password) or
        not re.search(r'[0-9]', password)):
        return jsonify({'message': 'Weak password'}), 400

    # Phone validation
    phone = data.get('phone')
    if phone and not re.match(r'^\+381\d{6,12}$', phone):
        return jsonify({'message': 'Invalid phone'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=hashed_password,
        phone=phone,
        address=data['address'],
        city=data['city']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    user = User.query.filter_by(email=data['email']).first()

    if not user:
        return jsonify({'message': 'Email does not exist'}), 404

    if not bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Wrong password'}), 401

    token = create_access_token(identity=str(user.id))

    return jsonify({
        'access_token': token,
        'user': {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': user.role
        }
    })
