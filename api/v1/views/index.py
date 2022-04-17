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
