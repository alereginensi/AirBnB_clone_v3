#!/usr/bin/python3
'''
It’s time to start our API!
'''

from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import Blueprint
from os import getenv
from flask import jsonify

app = Flask(__name__)


HOST = getenv('HBNB_API_HOST', '0.0.0.0')
PORT = getenv('HBNB_API_PORT', '5000')

# app_views = Blueprint('app_views', __name__, app)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(self):
    """Calls storage.close"""
    storage.close()

@app.teardown_appcontext
def error_not_found(self):
    """Custom 404"""
    return jsonify({"error": "Not found"})

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, threaded=True)
