import time
from pygame import mixer
from briefing import give_briefing


def wakeup():
    alarm()
    time.sleep(30)
    give_briefing()


def alarm():
    mixer.init()
    mixer.music.load("assets/alarm.mp3")
    mixer.music.play(3)


def __main__():
    # hoursToWake = int(open("../conf/hoursToWakeAt.txt", "r").read())
    # minsToWake = int(open("../conf/minsToWakeAt.txt", "r").read())
    # sched = BlockingScheduler()
    # sched.add_job(wakeup, 'cron', hour=hoursToWake, minute=minsToWake)
    # sched.start()
    # TODO: uncomment the above after debugging
    wakeup()
