# api/v1/views/__init__.py
from flask import Blueprint
from api.v1.views.index import *

<<<<<<< HEAD
# Blueprint creation should be after all imports
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
=======
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Importing views to register with the blueprint
from api.v1.views.index import *
>>>>>>> 4e72b6e78efa6938111d8958d04d3eec034cf233
