#!/usr/bin/python3
"""Flask App"""

from api.v1.views import app_views
from flask import Flask, render_template, jsonify, make_response
from models import storage
import os
from flask_cors import CORS


# create a variable app, instance of Flask
app = Flask(__name__)

# register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)

# A resource makes a cross-origin HTTP request
# when it requests a resource from a different domain, or port
# than the one the first resource itself serves.
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})

# flask env setup
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)


@app.teardown_appcontext
def teardown_db(exception):
    """calls storage.close() that
    on current sqlalchemy sessions
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """renders a custom error message for non-existent resources"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    """Run Flask"""
    app.run(host=host, port=port)
