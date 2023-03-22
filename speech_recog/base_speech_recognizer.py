import os
import re
import tempfile
from abc import ABC, abstractmethod

import requests
import googlesearch
from bs4 import BeautifulSoup
from gtts import gTTS


class BaseSpeechRecognizer(ABC):
    def __init__(self, language):
        self.language = language

    @abstractmethod
    def recognize_speech(self):
        pass

    def speak(self, text):
        if self.language == "pl":
            lang_code = "pl"
        elif self.language == "uk":
            lang_code = "uk"
        else:
            raise ValueError(f"Invalid language '{self.language}', use 'pl' or 'uk'.")

        tts = gTTS(text, lang = lang_code)
        with tempfile.NamedTemporaryFile(delete = True) as fp:
            tts.save(fp.name)
            os.system(f"afplay {fp.name}")

    def ask_for_city(self):
        if self.language == 'pl':
            self.speak("Dla jakiego miasta chcesz uzyskać informacje o jakości powietrza?")
        elif self.language == 'uk':
            self.speak("Для якого міста ви хочете дізнатися про якість повітря?")

        city = None
        while city is None:
            city = self.recognize_speech()
        return city

    def extract_city(self, query):
        if self.language == 'pl':
            match = re.search(r'pogoda\s+([\w\s]+)', query, re.IGNORECASE)
        elif self.language == 'uk':
            match = re.search(r'погода\s+([\w\s]+)', query, re.IGNORECASE)
        return match.group(1).strip() if match else None

    def search_google(self, query):
        search_results = googlesearch.search(query, num_results = 3)
        summaries = []
        for url in search_results:
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                summary = soup.find_all('p')[0].get_text()
                summaries.append(summary)
            except:
                pass
        return summaries