import speech_recognition as sr

from .base_speech_recognizer import BaseSpeechRecognizer

class PolishSpeechRecognizer(BaseSpeechRecognizer):
    def __init__(self):
        super().__init__('pl')
        self.recognizer = sr.Recognizer()

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Słucham...")
            audio = self.recognizer.listen(source,timeout = None)

        try:
            return self.recognizer.recognize_google(audio, language='pl-PL')
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
