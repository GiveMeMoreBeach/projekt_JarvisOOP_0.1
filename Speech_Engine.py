import pyttsx3
import speech_recognition as sr
import time


class Talk:
    def __init__(self):
        self.reconizer = sr.Recognizer()
        self.reconizer.pause_threshold = 0.8

    def _get_engine(self):
        sapi = pyttsx3.init()
        voices = sapi.getProperty('voices')
        sapi.setProperty('voice', voices[0].id)
        sapi.setProperty('rate', 170)
        sapi.setProperty('volume', 1.0)
        return sapi

    def talk(self,tekst):
        tekst1 = tekst.replace(".", " ")
        print(f"Jarvis: {tekst1}")
        sapi = self._get_engine()
        sapi.say(tekst1)
        sapi.runAndWait()
        time.sleep(0.5)



    def listen(self):

        with sr.Microphone() as source:
            print("Jarvis...")
            self.reconizer.adjust_for_ambient_noise(source,duration = 0.2)
            audio = self.reconizer.listen(source)
        try:
            print("Rozpoznaje...")
            zapytanie = self.reconizer.recognize_google(audio,language='pl-PL')
            print(f"{zapytanie}")
            return zapytanie.lower()
        except sr.UnknownValueError:
            print("Nie zrozumialem dzwieku")
            return ""
        except sr.RequestError:
            print("bład polaczenia z usluga rozpoznawania mowy")
            return ""


