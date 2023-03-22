import requests

class WeatherAPI:
    def __init__(self, api_key, language='pl'):
        self.api_key = api_key
        self.language = language

    def get_weather_data(self, lat, lon):
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}&units=metric&lang={self.language}"
        response = requests.get(url)
        if response.ok:
            data = response.json()
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return f"{temp}°C, {description}"
        else:
            return None
