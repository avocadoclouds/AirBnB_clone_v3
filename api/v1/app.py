#!/usr/bin/python3
"""Flask App"""

from flash import Flask, render_template
from models import storage
from api.v1.views import app_views
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

if __name__ == "__main__":
