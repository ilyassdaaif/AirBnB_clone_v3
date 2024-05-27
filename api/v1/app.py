#!/usr/bin/python3
<<<<<<< HEAD
"""
Create Flask app; and register the blueprint app_views to Flask instance app.
"""
from flask import Flask
=======
"""app"""
from flask import Flask, make_response, jsonify
>>>>>>> 7c42ad06336f696b5d90f30c5755a66cf841d511
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
<<<<<<< HEAD
=======
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


app.url_map.strict_slashes = False
>>>>>>> 7c42ad06336f696b5d90f30c5755a66cf841d511
app.register_blueprint(app_views)


@app.teardown_appcontext
<<<<<<< HEAD
def close_db(error):
    """Close database session"""
    storage.close()

if __name__ == "__main__":
    app.run(debug=True)
=======
def tear(self):
    ''' closes storage engine '''
    storage.close()


@app.errorhandler(404)
def not_found(error):
    ''' handles 404 error and gives json formatted response '''
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
>>>>>>> 7c42ad06336f696b5d90f30c5755a66cf841d511
