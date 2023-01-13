import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
import speak
from decouple import config
import speech_reco
IPSEARCH=config('IPLINK')
USERNAME=config('USER')
def myip():
    ip=requests.get(IPSEARCH).json()
    speak.speakout(ip["ip"])
    print(ip["ip"])
def wikipidea_search():
    query=speech_reco.input_from_user()
    try: 
        result=wikipedia.summary(query,sentences=2)
        print(result)
        speak.speakout(result)
    except Exception:
        speak.speakout(f"sorry {USERNAME} i cannot understand your command. Can you please say one more time?")
        wikipidea_search()  
def youtube_search():
    query=speech_reco.input_from_user()
    try: 
        kit.playonyt(query)
    except Exception:
        speak.speakout(f"sorry {USERNAME} i cannot understand your command. Can you please say one more time?")
        youtube_search()  