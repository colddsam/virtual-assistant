import openapplication as oa
import timeanddate as td
import speak
import online
from decouple import config
from operatingsystem import paths
USERNAME=config('USER')
BOTNAME=config('BOTNAME')
def make_dec(speech):
    if 'exit' in speech or 'stop' in speech or 'finish' in speech or 'turn off' in speech:
        return 0
    if 'wikipedia' in speech:
        speak.speakout(f"sure {USERNAME}, what you want to search?")
        online.wikipidea_search()
        return 1
    if 'youtube' in speech:
        speak.speakout(f"sure {USERNAME}, what you want to search?")
        online.youtube_search()
        return 1
    if 'open' in speech or 'start' in speech:
        oa.openapp(speech)
        return 1
    if 'you' in speech and 'love' in speech:
        speak.speakout(f"Wow! I am glad to hear that {USERNAME}. I also love you {USERNAME} as a friendly AI. Thank you to flirting with me.")
        return 1
    if 'i' in speech and 'sad' in speech:
        speak.speakout(f"don't cry in front of me. You should take some tissues")
        return 1
    if 'time' in speech:
        td.tell_time()
        return 1
    if 'ip' in speech and 'address' in speech:
        online.myip()
        return 1
    if 'what' in speech and 'you' in speech and 'can' in speech and 'do' in speech:
        speak.speakout(f"I am {BOTNAME}. Your personal virtual assistant. I can do any search on web. I cant sent messages and Email for you. I can also able to open application in your device.")
        return 1
    if 'favourite' in speech and 'app' in speech:
        speak.speakout(f"{USERNAME} your favorite applications are-")
        speak.speakout(paths.keys())
        return 1
    return 2

