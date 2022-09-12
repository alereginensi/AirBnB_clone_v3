#!/usr/bin/python3
'''
It’s time to start our API!
'''

from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import Blueprint
from os import getenv
from flask import jsonify, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

HOST = getenv('HBNB_API_HOST', '0.0.0.0')
PORT = getenv('HBNB_API_PORT', '5000')


app.register_blueprint(app_views)


@app.route("/*")
def post_example():
    """POST in server"""
    return jsonify(message="POST request returned")


@app.teardown_appcontext
def close_storage(self):
    """Calls storage.close"""
    storage.close()


@app.errorhandler(404)
def error_not_found(error):
    """Custom 404"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, threaded=True)
