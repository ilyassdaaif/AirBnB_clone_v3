# api/v1/views/index.py
from flask import jsonify
from api.v1.views import app_views

<<<<<<< HEAD

=======
>>>>>>> 4e72b6e78efa6938111d8958d04d3eec034cf233
@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
