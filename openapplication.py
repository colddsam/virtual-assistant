from operatingsystem import paths
import os
import speak
import subprocess as sp
from decouple import config
USERNAME=config('USER')
BOTNAME=config('BOTNAME') 
def openapp(speech):
    if 'code block' in speech:
        speak.speakout('opening codeblock')
        os.startfile(paths['codeblock'])
    elif 'chrome' in speech:
        speak.speakout('opening chrome')
        os.startfile(paths['chrome'])
    elif 'lensstudio' in speech:
        speak.speakout('opening lens studio')
        os.startfile(paths['lensstudio'])
    elif 'explorer' in speech:
        speak.speakout('opening file explorer')
        os.startfile(paths['explorer'])
    elif 'notepad' in speech:
        speak.speakout('opening notepad')
        os.startfile(paths['notepad'])
    elif 'proteus' in speech:
        speak.speakout('opening proteus')
        os.startfile(paths['proteus'])
    elif 'github desktop' in speech:
        speak.speakout('opening github desktop')
        os.startfile(paths['github desktop'])
    elif 'vs code' in speech:
        speak.speakout('opening vs code')
        os.startfile(paths['vs code'])
    elif 'command prompt' in speech:
        speak.speakout('opening command prompt')
        os.system('start cmd')
    elif 'camera' in speech:
        speak.speakout('opening camera')
        sp.run('start microsoft.windows.camera:', shell=True) 
    else:
        speak.speakout(f"sorry{USERNAME} this application is not in the list")

    