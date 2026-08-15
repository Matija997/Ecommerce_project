from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, bcrypt, jwt

from routes.auth import auth_bp
from routes.users import user_bp
from routes.admin import admin_bp
from routes.products import products_bp


app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# REGISTER ROUTES
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(products_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
