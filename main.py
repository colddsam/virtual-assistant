import timeanddate
import speech_reco
from decouple import config
import decision
import speak
USERNAME=config('USER')
BOTNAME=config('BOTNAME')
timeanddate.greeting_master()
cond=1
while cond:
    speech=speech_reco.input_from_user()
    speech=speech.lower()
    cond=decision.make_dec(speech)
    if cond==1:
        speak.speakout(f'Can i do anything else for you {USERNAME}?')
    elif cond==2:
        speak.speakout(f"sorry {USERNAME} i cannot understand your command. Can you please say one more time?")
    elif cond==0:
        speak.speakout(f"thanks {USERNAME} for using me. Have a great day.")