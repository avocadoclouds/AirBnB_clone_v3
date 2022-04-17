#!/usr/bin/python3
"""
flask route that returns a status response (json)
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage



@app_views.route('/status')
def status():
    """
    function for status route that returns the status.
    """
    response = {"status": "OK"}
    return jsonify(response)


@app_views.route('/stats')
def stat():
    """ function  to return count of objects """
    result = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User),
    }

    return jsonify(result)
