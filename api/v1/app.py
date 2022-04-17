#!/usr/bin/python3
"""Flask App"""

from api.v1.views import app_views
from flask import Flask, render_template, jsonify
from models import storage
import os

# create a variable app, instance of Flask
app = Flask(__name__)

# register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)

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
 def page_not_fount(exception):
     """Route to handle 404 status"""
     response= {"error": "Not found"}
     return jsonify(response), 404


if __name__ == "__main__":
    """Run Flask"""
    app.run(host=host, port=port)
