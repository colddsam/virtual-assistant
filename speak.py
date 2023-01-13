import pyttsx3
from decouple import config
USERNAME=config("USER")
BOTNAME=config("BOTNAME")
engine=pyttsx3.init('sapi5')
engine.setProperty('rate',170)
engine.setProperty('volume',1.0)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speakout(text):
    engine.say(text)
    engine.runAndWait()
