#!/usr/bin/python3
"""create blueprint"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

<<<<<<< HEAD
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
=======
if app_views is not None:
    from api.v1.views.index import *
    from api.v1.views.states import *
    from api.v1.views.cities import *
    from api.v1.views.amenities import *
    from api.v1.views.users import *
    from api.v1.views.places import *
    from api.v1.views.places_reviews import *
    from api.v1.views.places_amenities import *
>>>>>>> 7c42ad06336f696b5d90f30c5755a66cf841d511
