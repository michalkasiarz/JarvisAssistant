from opencage.geocoder import OpenCageGeocode

class GeocodingAPI:
    def __init__(self, api_key):
        self.geocoder = OpenCageGeocode(api_key)

    def get_coordinates(self, city):
        results = self.geocoder.geocode(city)
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return None, None
