from flask import jsonify, request
from models import User, db

def get_all():
    """Retrieve all users"""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

def create():
    """Create a new user"""
    data = request.json
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

def get_one(userId):
    """Retrieve a single user by ID"""
    user = User.query.get(userId)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())

def update(userId):
    """Update an existing user"""
    user = User.query.get(userId)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify(user.to_dict())

def delete(userId):
    """Delete a user"""
    user = User.query.get(userId)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})
