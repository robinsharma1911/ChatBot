import speech_recognition as sr
import pyttsx3
from pyaudio import *

lines = {
    'hello':'hii',
    'how are you':'fine',
    'what is your name':'chat bot'
    
}

r = sr.Recognizer()


def speak(sound):
    engine = pyttsx3.init()
    engine.say(sound)
    engine.runAndWait()

while(1):
    try:
        with sr.Microphone() as source:
            print('listening...')
            r.adjust_for_ambient_noise(source,duration=0.5)
            audio2 = r.listen(source)
            audio = r.recognize_sphinx(audio2,language='en-IN')
            sound = audio.lower()
            print(sound)
            for x in lines:
                if sound in x:
                    speak(lines[x])
    except Exception as e:
        file = 'say again'
        print(file)
        