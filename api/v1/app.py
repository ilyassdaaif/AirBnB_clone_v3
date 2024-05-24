# api/v1/app.py
from flask import Flask
from models import storage
from api.v1.views import app_views
import os
<<<<<<< HEAD


app = Flask(__name__)
app.register_blueprint(app_views)

=======

app = Flask(__name__)
app.register_blueprint(app_views)
>>>>>>> 4e72b6e78efa6938111d8958d04d3eec034cf233

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

<<<<<<< HEAD

=======
>>>>>>> 4e72b6e78efa6938111d8958d04d3eec034cf233
if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
