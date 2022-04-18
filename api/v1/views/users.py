#!/usr/bin/python3
"""Flask route that returns json status response"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.user import User


@app_views.route('/users', methods=['GET'])
def get_users():
    """Return information for all users"""
    users = []
    for user in storage.all("User").values():
        users.append(user.to_dict())
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Return info of a user with a user_id"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404, 'Not found')
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """delete a user with a user_id"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404, 'Not found')
    user.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/users', methods=['POST'])
def create_user():
    """create a new user"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'email' not in request.get_json():
        return make_response(jsonify({'error': 'Missing email'}), 400)
    if 'password' not in request.get_json():
        return make_response(jsonify({'error': 'Missing password'}), 400)
    user = User(**request.get_json())
    user.save()
    return make_response(jsonify(user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(self_id):
    """update a user"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404, 'Not found')
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, attr, val)
    user.save()
    return jsonify(user.to_dict())
