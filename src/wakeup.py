import time

from apscheduler.schedulers.blocking import BlockingScheduler
from pygame import mixer

from briefing import give_briefing


def wakeup():
    """
    sound an alarm to wake up the user then give them their briefing.
    """
    alarm()
    time.sleep(30)
    give_briefing()


def alarm():
    """
    sound an alarm sound for ~ 30 seconds.
    """
    mixer.init()
    mixer.music.load("assets/alarm.mp3")
    mixer.music.play(3)


"""
ad-hoc main method.
get the time to wake the user up from config files.
then schedule a cron job to do so with the wakeup() method at that time.
"""
hoursToWake = int(open("../conf/hours_to_wake_at.txt", "r").read())
minsToWake = int(open("../conf/mins_to_wake_at.txt", "r").read())
sched = BlockingScheduler()
sched.add_job(wakeup, 'cron', hour=hoursToWake, minute=minsToWake)
sched.start()
