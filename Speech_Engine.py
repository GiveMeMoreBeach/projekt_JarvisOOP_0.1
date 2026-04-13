import pyttsx3
import speech_recognition as sr


class Talk:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.reconizer = sr.Recognizer()


        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 170)
        self.engine.setProperty('volume', 1.0)

        self.reconizer.pause_threshold = 0.8


    def talk(self,tekst):
        tekst1 = tekst.replace(".", " ")
        print(f"Jarvis: {tekst1}")
        self.engine.say(tekst1)
        self.engine.runAndWait()



    def listen(self):

        with sr.Microphone() as source:
            print("Jarvis...")
            self.reconizer.adjust_for_ambient_noise(source,duration = 0.2)
            audio = self.reconizer.listen(source)

        try:
            print("Rozpoznaje...")
            query = self.reconizer.recognize_google(audio,language='pl-PL')
            print(f"{query}")
            return query.lower()

        except sr.UnknownValueError:
            print("Nie zrozumialem dzwieku")
            return ""

        except sr.RequestError:
            print("bład polaczenia z usluga rozpoznawania mowy")
            return ""
