#!/usr/bin/python3
"""
view for the link between Place objects and Amenity objects that handles
all default RestFul API actions
"""
from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity

@app_views.route('/places/<place_id>/amenities', methods=['GET'], strict_slashes=False)
@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE', 'POST'], strict_slashes=False)
def handle_places_amenities(place_id, amenity_id=None):
    """
    Retrieves the list of all Amenity objects of a Place,
    delete or create an Amenity object of a Place
    """
    place_obj = storage.get("Place", place_id)
    if not place_obj:
        abort(404, description="Place not found")

    if request.method == 'GET' and not amenity_id:
        return jsonify([amenity_obj.to_dict() for amenity_obj in place_obj.amenities]), 200

    amenity_obj = storage.get("Amenity", amenity_id)
    if not amenity_obj:
        abort(404, description="Amenity not found")

    if request.method == 'DELETE':
        if amenity_obj not in place_obj.amenities:
            abort(404, description="Amenity is not linked to this Place")
        place_obj.amenities.remove(amenity_obj)
        storage.save()
        return '', 204

    if request.method == 'POST':
        if amenity_obj in place_obj.amenities:
            return jsonify(amenity_obj.to_dict()), 200
        place_obj.amenities.append(amenity_obj)
        place_obj.save()
        return jsonify(amenity_obj.to_dict()), 201
