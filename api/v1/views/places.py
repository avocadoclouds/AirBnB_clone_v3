#!/usr/bin/python3
"""
This module creates a new view for Place objects
that handles all default RESTFul API actions:
"""
from api.v1.views import app_views
from flask import jsonify, make_response, request, abort
from models import storage
from models.place import Place
from models.city import City
from models.state import State


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def retrieve_places(city_id):
    """returns all places for a particular city."""
    city = storage.get("City", city_id)
    if city is None:
        abort(404, 'Not found')
    places = []
    for place in city.places:
        places.append(place.to_dict())
    return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'])
def retrieve_place(place_id):
    """returns information about a particular place"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404, 'Not found')
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """deletes a place object"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404, 'Not found')
    place.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """creates a new place"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404, 'Not found')
    kwargs = request.get_json()
    if not kwargs:
        return make_response(jsonify({'error': 'Not a JSON'}), 404)
    if 'user_id' not in kwargs.keys():
        return make_response(jsonify({'error': 'Missing user_id'}), 404)
    user = storage.get("User", kwargs['user_id'])
    if not user:
        abort(404, 'Not found')
    if 'name' not in kwargs.keys():
        return make_response(jsonify({'error': 'Missing name'}), 404)
    kwargs['city_id'] = city_id
    place = Place(**kwargs)
    place.save()
    return make_response(jsonify(place.to_dict()), 201)


@app_views.route('places/<place_id>', methods=['PUT'])
def update_place(place_id):
    """updates a place"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404, 'Not found')
    kwargs = request.get_json()
    if not kwargs:
        return make_response(jsonify({'error': 'Not a JSON'}), 404)
    for attr, val in kwargs.items():
        if attr not in ['id', 'user_id', 'city_id',
                        'created_at', 'updated_at']:
            setattr(place, attr, val)
    place.save()
    return jsonify(place.to_dict())
