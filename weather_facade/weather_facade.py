from api.geocoding_api import GeocodingAPI
from api.weather_api import WeatherAPI
from api.air_pollution_api import AirPollutionAPI


class WeatherFacade:
    def __init__(self, language, geocoding_api_key, weather_api_key, air_pollution_api_key):
        self.language = language
        self.geocoding_api = GeocodingAPI(geocoding_api_key)
        self.weather_api = WeatherAPI(weather_api_key)
        self.air_pollution_api = AirPollutionAPI(air_pollution_api_key)

    def get_weather_data(self, city):
        lat, lon = self.geocoding_api.get_coordinates(city)
        if lat is None or lon is None:
            return None, None

        weather_data = self.weather_api.get_weather(city, self.language)
        air_pollution_data = self.air_pollution_api.get_air_pollution_data(lat, lon)

        return weather_data, air_pollution_data

    def get_coordinates(self, city):
        results = self.geocoder.geocode(city)
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return None, None
