from briefing import giveBriefing
from pygame import mixer
import time

def wakeup():
    alarm()
    time.sleep(30)
    giveBriefing()

def alarm():
    mixer.init()
    mixer.music.load("alarm.mp3")
    mixer.music.play()

wakeup()