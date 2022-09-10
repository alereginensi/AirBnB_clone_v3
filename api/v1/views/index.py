#!/usr/bin/python3
'''
index
'''
from models.engine.file_storage import classes
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def index():
    """returns status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count():
    """Calls count method"""
    return jsonify(storage.count(classes['Amenity']))
# if __name__ == '__main__':
#    app.run(host='0.0.0.0', port='5000')
