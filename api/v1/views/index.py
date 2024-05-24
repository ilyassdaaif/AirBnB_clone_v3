#!/usr/bin/python3
"""
"""
from . import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    """ Return a JSON response indicating the status of the API. """
    return jsonify(status="OK")
