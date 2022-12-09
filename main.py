import pyttsx3 as tts
import speech_recognition as sr
import os
import time
from datetime import datetime
import wikipedia
import webbrowser
import random

film=["Breaking Bad","The Walking Dead","Mr.Robot","Titanic","Pirates of Carribean"]



engine = tts.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def main():
    r=sr.Recognizer()
    with sr.Microphone() as source2:
        print("Say something...")
        r.adjust_for_ambient_noise(source2)
        audio2 = r.listen(source2,None,3)
        print("the audio has been recorded")
        MyText=sr.Recognizer.recognize_google(audio2)
        MyText=MyText.lower()
    if "who is" in MyText:
        person=MyText.replace("who is","")
        try:
            info=wikipedia.summary(person,1)
            print(info)
            talk(info)
        except:
            speak("I dont understand")

    elif "Hi" in MyText:
        speak("Hello how i can help you?")

    elif "How are you?" in MyText:
        speak("I am good thank you")

    elif "Who created you?" in MyText:
        speak("I am created by Hudulov")
        
    elif "Open Web site named" in MyText:
        web=MyText.replace("Open Web site named","")
        try:
            webbrowser.open('http://'+MyText, new=2)
        except:
            speak("I dont understand")
        
    elif "Why you created ?" in MyText:
        speak("I am created for help you")
        
    elif "Suggest me Film" in MyText:
        filmname = random.randint(0, len(film)+1)
        speak(filmname)
        
    elif "What is time" in MyText:
        speak("Hello how i can help you?")

    elif "Hi" in MyText:
        speak("Hello how i can help you?")
    


        
    elif MyText=="":
        speak("I dont understand")
        

while True:
    main()
    time.sleep(10)

