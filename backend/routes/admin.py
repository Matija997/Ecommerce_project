from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User

admin_bp = Blueprint('admin', __name__)


def admin_required():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    if user.role != "admin":
        return jsonify({"message": "Forbidden"}), 403

    return user


@admin_bp.route('/admin/check', methods=['GET'])
@jwt_required()
def admin_check():

    user = admin_required()

    return jsonify({
        "message": "Welcome admin",
        "email": user.email
    })
