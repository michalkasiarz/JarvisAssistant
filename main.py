from weather_facade.weather_facade import WeatherFacade
from speech_recog.polish_speech_recognizer import PolishSpeechRecognizer
from speech_recog.ukrainian_speech_recognizer import UkrainianSpeechRecognizer
from config import GEOCODING_API_KEY, WEATHER_API_KEY, AIR_POLLUTION_API_KEY


def main():
    language = input("Wybierz język (wpisz 'pl' dla polskiego, 'uk' dla ukraińskiego): ")
    if language == 'pl':
        recognizer = PolishSpeechRecognizer()
    elif language == 'uk':
        recognizer = UkrainianSpeechRecognizer()
    else:
        print("Nieprawidłowy język.")
        return

    while True:
        query = recognizer.recognize_speech()
        if query is None:
            recognizer.speak("Przepraszam, nie rozumiem.")
            continue

        weather_facade = WeatherFacade(language, GEOCODING_API_KEY, WEATHER_API_KEY, AIR_POLLUTION_API_KEY)
        if "jakość powietrza" in query or "zanieczyszczenie powietrza" in query or "якість повітря" in query or "забруднення повітря" in query:
            recognizer.speak("Dla jakiego miasta chcesz uzyskać informacje o jakości powietrza?")
            city = recognizer.recognize_speech()
            print(f"City: ", city)
            if city:
                weather_data, air_pollution_data = weather_facade.get_weather_data(city)
                if air_pollution_data:
                    recognizer.speak(f"Jakość powietrza w {city}: {air_pollution_data['air_quality']}. Norma PM2.5 przekroczona o {air_pollution_data['pm25_exceeded']:.2f}%, norma PM10 przekroczona o {air_pollution_data['pm10_exceeded']:.2f}%")
                else:
                    recognizer.speak("Nie udało się pobrać danych o jakości powietrza.")
            else:
                recognizer.speak("Nie udało się rozpoznać nazwy miasta.")
        elif "pogoda" in query or "погода" in query:
            city = recognizer.extract_city(query)
            if city:
                result = weather_facade.get_weather_data(city)
                if result is not None:
                    weather_data, _ = result
                    if weather_data is not None:
                        recognizer.speak(f"Pogoda w {city}: {weather_data}")
                    else:
                        recognizer.speak("Nie udało się pobrać danych o pogodzie.")
                else:
                    recognizer.speak("Nie udało się pobrać danych o pogodzie.")
            else:
                recognizer.speak("Nie udało się rozpoznać nazwy miasta.")
        else:
            summaries = recognizer.search_google(query)
            if summaries:
                for i, summary in enumerate(summaries, start = 1):
                    recognizer.speak(f"Wynik {i}: {summary}")
            else:
                recognizer.speak("Nie znaleziono żadnych informacji na ten temat.")


if __name__ == "__main__":
    main()
