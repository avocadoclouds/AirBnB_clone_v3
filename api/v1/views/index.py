#!/usr/bin/python3
"""import app_views from api.v1.views
create a route /status on the object app_views that
returns a JSON: "status": "OK"
"""

from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status')
def status():
    """
    function for status route that returns the status.
    """
    response = {"status": "OK"}
    return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def stats():
    """ function  to return count of objects."""
    if request.method == 'GET':
        response = {}
        result = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in result.items():
            response[value] = storage.count(key)
        return jsonify(response)
