from flask import Blueprint, request, jsonify
from models import Property, User
from database import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/add_property', methods=['POST'])
def add_property():
    data = request.json
    prop = Property(
        title=data['title'],
        price=data['price'],
        location=data['location'],
        description=data['description'],
        image_url=data['image_url']
    )
    db.session.add(prop)
    db.session.commit()
    return jsonify({"message": "Property added successfully"})

@admin_bp.route('/admin/delete_property/<int:id>', methods=['DELETE'])
def delete_property(id):
    prop = Property.query.get(id)
    if not prop:
        return jsonify({"error": "Property not found"}), 404
    db.session.delete(prop)
    db.session.commit()
    return jsonify({"message": "Property deleted"})
