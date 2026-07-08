from app import app
from extensions import db, bcrypt
from models.user import User


with app.app_context():

    # Create tables if they don't exist
    db.create_all()

    # Check if admin already exists
    existing_admin = User.query.filter_by(
        email="admin@test.com"
    ).first()

    if existing_admin:
        print("Admin already exists!")
    else:
        admin = User(
            first_name="Admin",
            last_name="User",
            email="admin@test.com",
            password=bcrypt.generate_password_hash(
                "Admin123"
            ).decode('utf-8'),
            phone="+381601234567",
            address="Admin Street",
            city="Belgrade",
            role="admin"
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin created successfully!")