import webbrowser
import pyttsx3 as tts
import speech_recognition as sr
import wikipedia
import wikipedia
from datetime import datetime
engine = tts.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
speak("Current Time =", current_time)