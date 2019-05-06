from flask.blueprints import Blueprint
from traceback import format_exc
from .handler import GetDistance
from flask import request

distance = Blueprint('distance', __name__)


@distance.route('/get_distance', methods=['POST'])
def get_distance():
    try:
        data = request.json()
        return GetDistance().get_distance_between_two_gps_points(data)
    except Exception as error:
        print('Exception in get distance..:' + str(error))
        print(format_exc().splitlines())
        return None


