#!/usr/bin/python3
"""
flask route that returns a status response (json).
"""

from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """
    function for status route that returns the status.
    """
    if request.method == 'GET':
        response = {"status": "OK"}
        return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def stats():
    """ function  to return count of objects """
    if request.method == 'GET':
        result = {
            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
        }

        return jsonify(result)
