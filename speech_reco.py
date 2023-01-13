import speech_recognition as sr
import speak
from decouple import config
USERNAME=config("USER")
BOTNAME=config("BOTNAME")

def input_from_user():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
    except Exception:
        speak.speakout(f"sorry {USERNAME} i cannot able to recognize any voice.")
        query='none'
    return query