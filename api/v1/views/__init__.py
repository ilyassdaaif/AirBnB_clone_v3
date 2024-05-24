#!/usr/bin/python3
"""
Module that sets up the Flask application and registers the blueprint
"""
from flask import Blueprint

# Ensure that all imports are at the top of the file
from api.v1.views.index import *

# Define the Blueprint after all imports
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
