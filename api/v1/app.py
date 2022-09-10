#!/usr/bin/python3
'''
It’s time to start our API!
'''

from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import Blueprint
app = Flask(__name__)

app_views = Blueprint('app_views', app)

def create_app():
    with app.app_context():
        storage.close()

    return app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True)
