import requests


class AirPollutionAPI:
    PM25_STANDARD = 25
    PM10_STANDARD = 50
    AQI_DESCRIPTIONS = {
        'pl': {
            1: "Bardzo dobra",
            2: "Dobra",
            3: "Umiarkowana",
            4: "Zła",
            5: "Bardzo zła",
        },
        'uk': {
            1: "Дуже добра",
            2: "Добра",
            3: "Середня",
            4: "Погана",
            5: "Дуже погана",
        }
    }

    def __init__(self, api_key, language = 'pl'):
        self.api_key = api_key
        self.language = language

    def _get_air_pollution(self, lat, lon):
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_air_pollution_data(self, lat, lon):
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            components = data["list"][0]["components"]
            main_data = data["list"][0]["main"]

            air_quality_index = main_data["aqi"]
            pm25_exceeded = ((components["pm2_5"] / self.PM25_STANDARD) - 1) * 100
            pm10_exceeded = ((components["pm10"] / self.PM10_STANDARD) - 1) * 100

            return {
                "air_quality": self.AQI_DESCRIPTIONS[self.language][air_quality_index],
                "pm25_exceeded": pm25_exceeded,
                "pm10_exceeded": pm10_exceeded,
            }
        else:
            return None

