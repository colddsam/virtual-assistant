from datetime import datetime
from decouple import config
import speak
USERNAME=config("USER")
BOTNAME=config("BOTNAME")
hour=datetime.now().hour
def greeting_master():
    if hour>=6 and hour<12:
        speak.speakout(f"Good morning {USERNAME}")
    elif hour>=12 and hour<16:
        speak.speakout(f"Good Afternoon {USERNAME}")
    elif hour>=16 and hour<19:
        speak.speakout(f"Good Evening {USERNAME}")
    else:
        speak.speakout(f"It's a great night {USERNAME}")
    speak.speakout(f"I am {BOTNAME} your personal virtual assistant. How can i help you?")
def tell_time():
    if datetime.now().hour>12:
        speak.speakout(f"{USERNAME} it's now {datetime.now().hour-12} PM with {datetime.now().minute} minutes ")
    elif datetime.now().hour==12:
        speak.speakout(f"{USERNAME} it's now {datetime.now().hour} PM with {datetime.now().minute} minutes ")
    else:
        speak.speakout(f"{USERNAME} it's now {datetime.now().hour} AM with {datetime.now().minute} minutes ")