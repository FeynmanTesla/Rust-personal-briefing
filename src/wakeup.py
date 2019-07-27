import time
from pygame import mixer
from briefing import give_briefing
from apscheduler.schedulers.blocking import BlockingScheduler


def wakeup():
    alarm()
    time.sleep(30)
    give_briefing()


def alarm():
    mixer.init()
    mixer.music.load("assets/alarm.mp3")
    mixer.music.play(3)


hoursToWake = int(open("../conf/hours_to_wake_at.txt", "r").read())
minsToWake = int(open("../conf/mins_to_wake_at.txt", "r").read())
sched = BlockingScheduler()
sched.add_job(wakeup, 'cron', hour=hoursToWake, minute=minsToWake)
sched.start()
