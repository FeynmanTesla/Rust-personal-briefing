from briefing import give_briefing
from pygame import mixer
import time
from apscheduler.schedulers.blocking import BlockingScheduler


def wakeup():
    alarm()
    time.sleep(30)
    give_briefing()


def alarm():
    mixer.init()
    mixer.music.load("alarm.mp3")
    mixer.music.play(3)


def __main__():
    hoursToWake = int(open("conf/hoursToWakeAt.txt", "r").read())
    minsToWake = int(open("conf/minsToWakeAt.txt", "r").read())
    sched = BlockingScheduler()
    sched.add_job(wakeup, 'cron', hour=hoursToWake, minute=minsToWake)
    sched.start()
