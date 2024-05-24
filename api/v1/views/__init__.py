# api/v1/views/__init__.py
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Importing views to register with the blueprint
from api.v1.views.index import *
