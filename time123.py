import webbrowser
import pyttsx3 as tts
import speech_recognition as srz
from datetime import datetime
engine = tts.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
now = datetime.now()
speak(now.strftime("%H:%M:%S"))
