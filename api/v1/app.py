#!/usr/bin/python3
"""
"""
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_schema(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """ Close the database/storage session. """
    storage.close()


if __name__ == "__main__":
    import os
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)