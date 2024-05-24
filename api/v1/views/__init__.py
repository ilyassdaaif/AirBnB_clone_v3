#!/usr/bin/python3
"""
"""
from flask import Blueprint
from . import index  # This line is causing the issue.

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Normally, it's advised to handle imports at the top,
# but due to Flask's structure,
# it might be necessary to keep some imports below the Blueprint creation.
