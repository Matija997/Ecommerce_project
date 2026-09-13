from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from extensions import db
from models.contact_message import ContactMessage
from validators import validate_email_format
from routes.admin import get_admin_or_error

contact_bp = Blueprint('contact', __name__)

REQUIRED_FIELDS = ['name', 'email', 'message']


@contact_bp.route('/contact', methods=['POST'])
def submit_contact():
    data = request.json or {}

    for field in REQUIRED_FIELDS:
        value = data.get(field)
        if not isinstance(value, str) or not value.strip():
            return jsonify({'message': f'{field} is required'}), 400

    if not validate_email_format(data['email']):
        return jsonify({'message': 'Invalid email'}), 400

    entry = ContactMessage(
        name=data['name'].strip(),
        email=data['email'].strip(),
        message=data['message'].strip()
    )
    db.session.add(entry)
    db.session.commit()

    return jsonify({'message': 'Message sent'}), 201


@contact_bp.route('/admin/messages', methods=['GET'])
@jwt_required()
def list_messages():
    _, error = get_admin_or_error()
    if error:
        return error

    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return jsonify([m.to_dict() for m in messages])


@contact_bp.route('/admin/messages/<int:message_id>', methods=['DELETE'])
@jwt_required()
def delete_message(message_id):
    _, error = get_admin_or_error()
    if error:
        return error

    entry = ContactMessage.query.get(message_id)
    if not entry:
        return jsonify({'message': 'Message not found'}), 404

    db.session.delete(entry)
    db.session.commit()

    return jsonify({'message': 'Message deleted'})
