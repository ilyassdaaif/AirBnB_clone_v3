# api/v1/views/__init__.py
from flask import Blueprint
from api.v1.views.index import *

# Blueprint creation should be after all imports
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
