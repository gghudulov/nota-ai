import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

r = sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def recordMyCommand():
    try:
        with sr.Microphone() as source:                # use the default microphone as the audio source
            print("Listening.....")
            audio = r.listen(source)
            command=r.recognize_google(audio)
            command=command.lower() 
            if 'alexa' in command:
                command=command.replace("alexa","")
                print(command)
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")
    return command



def getNumber(ph):
    print(ph)
    number="+"
    for i in ph:
        if(i.isdigit()):

            number+=i
    print(number)
    return number


def getActualMessage(cmd):
    print(cmd)
    newmsg=""
    for i in cmd:
        if(not i.isdigit()):
            newmsg+=i
    print(newmsg)    
    return newmsg

def alexa_listen():

    command=recordMyCommand()
    print(command)

    if "play" in command:
        song=command.replace("play","")
        talk("playing"+song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is"+time)
        print(time)

    elif "who is" in command:
        person=command.replace("who is","")
        try:
            info=wikipedia.summary(person,1)
            print(info)
            talk(info)
        except:
            talk("Sorry, I did not found anything about"+person +"on wikipedia")


    elif "whatsapp" in command:
        talk("Tell me your message that you want to send and receiver contact number ")
        try:
            with sr.Microphone() as source:                # use the default microphone as the audio source
                print("Listening.....")
                msg = r.listen(source)
                command=r.recognize_google(msg)
                command=command.lower()
                pywhatkit.sendwhatmsg_instantly(getNumber(command),getActualMessage(command))
               
        except LookupError:                            # speech is unintelligible
            print("Could not understand audio")

    else:
        talk("Hey, Could you just say the command again?")

         
while True:
    alexa_listen()
