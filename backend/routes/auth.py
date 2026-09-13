from flask import Blueprint, request, jsonify, current_app
from extensions import db, bcrypt
from flask_jwt_extended import create_access_token
from models.user import User
import re
import json
import secrets
import urllib.request
import urllib.error
import urllib.parse

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json

    # Required fields
    required_fields = ['first_name', 'last_name', 'email', 'password',
                       'phone', 'address', 'city']
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
    phone = data['phone']
    if not re.match(r'^\+381\d{6,12}$', phone):
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
    data = request.json or {}

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'Email does not exist'}), 404

    if not bcrypt.check_password_hash(user.password, password):
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


@auth_bp.route('/auth/google', methods=['POST'])
def google_auth():
    data = request.json or {}
    credential = data.get('credential')

    if not credential:
        return jsonify({'message': 'Missing Google credential'}), 400

    query = urllib.parse.urlencode({'id_token': credential})
    try:
        with urllib.request.urlopen(
            f'https://oauth2.googleapis.com/tokeninfo?{query}', timeout=5
        ) as resp:
            payload = json.loads(resp.read())
    except urllib.error.HTTPError:
        return jsonify({'message': 'Invalid Google token'}), 401
    except urllib.error.URLError:
        return jsonify({'message': 'Could not reach Google to verify token'}), 502

    if payload.get('aud') != current_app.config['GOOGLE_CLIENT_ID']:
        return jsonify({'message': 'Google token was not issued for this app'}), 401

    if payload.get('email_verified') != 'true':
        return jsonify({'message': 'Google email is not verified'}), 401

    email = payload['email']
    user = User.query.filter_by(email=email).first()

    if not user:
        random_password = bcrypt.generate_password_hash(
            secrets.token_hex(32)
        ).decode('utf-8')
        user = User(
            first_name=payload.get('given_name', ''),
            last_name=payload.get('family_name', ''),
            email=email,
            password=random_password
        )
        db.session.add(user)
        db.session.commit()

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
