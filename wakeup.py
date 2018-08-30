from briefing import giveBriefing
from pygame import mixer
import time
from apscheduler.schedulers.blocking import BlockingScheduler
hoursToWake = int(open("hoursToWakeAt.txt","r").read())
minsToWake = int(open("minsToWakeAt.txt","r").read())

def wakeup():
    alarm()
    giveBriefing()

def alarm():
    mixer.init()
    mixer.music.load("alarm.mp3")
    mixer.music.play(3)

sched = BlockingScheduler()

# Schedules wakeup alarm at 8 AM every day
sched.add_job(wakeup, 'cron', hour=hoursToWake, minute=minsToWake)

sched.start()
