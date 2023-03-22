from geopy.geocoders import Nominatim
from api.weather_api import WeatherAPI
from api.air_pollution_api import AirPollutionAPI


class WeatherFacade:
    def __init__(self, language, geocoding_api_key, weather_api_key, air_pollution_api_key):
        self.language = language
        self.geocoding_api_key = geocoding_api_key
        self.weather_api_key = weather_api_key
        self.air_pollution_api_key = air_pollution_api_key
        self.geolocator = Nominatim(user_agent = "weather_app")
        self.weather_api = WeatherAPI(weather_api_key, language)
        self.air_pollution_api = AirPollutionAPI(air_pollution_api_key, language)

    def get_weather_data(self, city):
        location = self.geolocator.geocode(city)
        if not location:
            return None

        lat, lon = location.latitude, location.longitude
        weather_data = self.weather_api.get_weather_data(lat, lon)
        air_pollution_data = self.air_pollution_api.get_air_pollution_data(lat, lon)

        return weather_data, air_pollution_data

