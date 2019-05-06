from traceback import format_exc
from geopy.distance import distance
from geopy.geocoders import Nominatim


class GetDistance:
    """
    This calss is used to get shortest path between two points
    """
    def __index__(self, for_search=False):
        """
        Default Constructor
        :return:
        """
        self.geo_locator = None
        if for_search:
            self.geo_locator = Nominatim('destination')

    def get_distance_between_two_gps_points(self, data):
        """
        This method is used to get distance between two geo points
        :param data:
        Dict('start_point': {'longitude': <float>, 'latitude': <float>},
             'end_point': {'longitude': <float>, 'latitude': <float>})
        :return: distance between points in kms
        """
        try:
            start_point = (data.get('start_point').get('latitude'), data.get('start_point').get('longitude'))
            end_point = (data.get('end_point').get('latitude'), data.get('end_point').get('longitude'))
            return distance(start_point, end_point).kilometers
        except Exception as error:
            print('Exception in get distance..:' + str(error))
            print(format_exc().splitlines())
            return None

    def get_lat_log_from_address(self, address):
        """
        This method is used to get longitude and latitude from address
        :param address:
        :return: latitude, longitude
        """
        try:
            location = self.geo_locator.geocode(address)
            return location.latitude, location.longitude
        except Exception as error:
            print('Exception in get distance..:' + str(error))
            print(format_exc().splitlines())
            return None

    def get_address_from_lat_long(self, location):
        """
        This method is used to get longitude and latitude from address
        :param location:
        :return: latitude, longitude
        """
        try:
            location = self.geo_locator.reverse(str(location.get('latitude')) + ', ' + str(location.get('longitude')))
            return location.address
        except Exception as error:
            print('Exception in get distance..:' + str(error))
            print(format_exc().splitlines())
            return None
