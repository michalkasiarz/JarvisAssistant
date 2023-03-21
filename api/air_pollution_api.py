import requests

class AirPollutionAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_air_pollution_data(self, lat, lon):
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url)

        if response.ok:
            data = response.json()
            if 'current' in data and 'values' in data['current'] and len(data['current']['values']) > 0:
                pm25 = data['current']['values'][0]['value']
            else:
                pm25 = None

            return pm25
        else:
            return None
