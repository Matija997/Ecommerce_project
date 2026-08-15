from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User

admin_bp = Blueprint('admin', __name__)


def get_admin_or_error():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return None, (jsonify({"message": "User not found"}), 404)

    if user.role != "admin":
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
