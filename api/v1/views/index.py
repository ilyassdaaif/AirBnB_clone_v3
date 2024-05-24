#!/usr/bin/python3
"""
Module that defines the index view for the API
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
