from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
import re

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    city = db.Column(db.String(30))


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json

    # Required fields
    required_fields = ['first_name', 'last_name', 'email', 'password',
                       'address', 'city']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'message': f'{field.replace("_", " ").title()}'
                            ' is required'}), 400

    # Email format
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, data['email']):
        return jsonify({'message': 'Invalid email format'}), 400

    # Check if email already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400

    # Password strength
    password = data['password']
    if (len(password) < 8 or
        not re.search(r'[A-Z]', password) or
        not re.search(r'[a-z]', password) or
        not re.search(r'[0-9]', password)):
        return jsonify({
            'message': 'Password must be at least 8 characters long'
            ' and include an uppercase letter, a lowercase letter, and number'
        }), 400

    # Optional: phone number validation (digits only)
    phone = data.get('phone')
    if phone and not re.match(r'^\+381\d{6,12}$', phone):
        return jsonify({'message': 'Invalid phone number'}), 400

    # Hash password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create user
    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=hashed_password,
        phone=data.get('phone'),
        address=data.get('address'),
        city=data.get('city')
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        return jsonify({'message': 'Email does not exist'}), 404

    if not bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Wrong password'}), 401

    token = create_access_token(identity=user.id)

    return jsonify({
        'message': 'Login successful',
        'access_token': token,
        'user': {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }
    })


@app.route('/profile')
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({
        'email': user.email,
        'first_name': user.first_name
    })


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
