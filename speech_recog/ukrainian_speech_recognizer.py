import speech_recognition as sr

from .base_speech_recognizer import BaseSpeechRecognizer

class UkrainianSpeechRecognizer(BaseSpeechRecognizer):
    def __init__(self):
        super().__init__('uk')
        self.recognizer = sr.Recognizer()

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Слухаю...")
            audio = self.recognizer.listen(source, timeout=None)

        try:
            return self.recognizer.recognize_google(audio, language='uk-UA')
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
