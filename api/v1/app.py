#!/usr/bin/python3
"""
Create Flask app; and register the blueprint app_views to Flask instance app.
"""
import sys
import os
from os import getenv
from flask import Flask, jsonify

# Add the project directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_engine(exception):
    """
    Close the storage engine.
    """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors with a custom JSON response.
    """
    response = {"error": "Not found"}
    return jsonify(response), 404

if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(debug=True, host=HOST, port=PORT, threaded=True)
