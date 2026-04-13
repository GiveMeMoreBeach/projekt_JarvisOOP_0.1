import os
import shutil
import pyttsx3
from send2trash import send2trash
import time
import webbrowser

class Talk:
    def talk(self,tekst):
        tekst1 = tekst.replace(".", " ")
        print(f"Jarvis: {tekst1}")
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)
        engine.say(tekst1)
        engine.runAndWait()
        del engine