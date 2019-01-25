import reverse_geocoder as rg
import geopy.distance as g


class LocationHelper:
    @staticmethod
    def get_location(lat, long):
        try:
            result = rg.search((lat, long))[0]
            return result['name']+", "+result['admin1']
        except Exception as e:
            return {'data': [], 'status': 'failed', 'message': str(e)}

    @staticmethod
    def get_distance(source_lat, source_long, destination_lat, destination_long):
        try:
            distance = g.vincenty((source_lat, source_long), (destination_lat, destination_long)).km
            return distance
        except Exception as e:
            return {'data': [], 'status': 'failed', 'message': str(e)}

