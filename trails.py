from flask import request, jsonify
from models import Trail, db
from datetime import datetime
import pytz


def get_all():
    trails = Trail.query.all()
    return jsonify([trail.to_dict() for trail in trails])

def create():
    data = request.json
    new_trail = Trail(**data)
    db.session.add(new_trail)
    db.session.commit()
    return jsonify(new_trail.to_dict()), 201

def get_one(trailId):
    trail = Trail.query.get(trailId)
    if not trail:
        return jsonify({"error": "Trail not found"}), 404
    return jsonify(trail.to_dict())

def update(trailId):
    trail = Trail.query.get(trailId)
    if not trail:
        return jsonify({"error": "Trail not found"}), 404

    data = request.json
    for key, value in data.items():
        setattr(trail, key, value)
    db.session.commit()
    return jsonify(trail.to_dict())

def delete(trailId):
    trail = Trail.query.get(trailId)
    if not trail:
        return jsonify({"error": "Trail not found"}), 404

    db.session.delete(trail)
    db.session.commit()
    return jsonify({"message": "Trail deleted"})
