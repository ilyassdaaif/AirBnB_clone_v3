#!/usr/bin/python3
"""create users etc ..."""
from flask import jsonify, request, abort
from models import storage
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_user():
    """ Retrieves the list of all User objects """
    users = [user.to_dict() for user in storage.all("User").values()]
    return jsonify(users)


@app_dispatch.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves a User object """
    user = storage.get("User", user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """ Create a User """
    body = request.get_json(silent=True)
    if body is None:
        abort(400, description="Not a JSON")
    if 'email' not in body:
        abort(400, description="Missing email")
    if 'password' not in body:
        abort(400, description="Missing password")
    user = User(**body)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """ Updates a User object """
    user = storage.get("User", user_id)
    if not user:
        abort(404)
    body = request.get_json(silent=True)
    if body is None:
        abort(400, description="Not a JSON")
    for key, value in body.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ Deletes a User object """
    user = storage.get("User", user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200
