from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def status():
    """
    function for status route that returns the status
    """
    response = {"status": "OK"}
    return jsonify(response)
