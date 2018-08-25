import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pyttsx
engine = pyttsx.init()

from getGmailEmails import getGmailEmails
from getNews import getNews
from getGreeting import getGreeting
from getWeather import getWeather
from getDateTime import getDateTime, datetime
from getEvents import getEvents
from getOffice365Emails import getOffice365Emails

# TODO: clean up code, split and abstract methods
# TODO: ensure all methods in all source code files are <= 20 lines each
# TODO: add error handling
# TODO: update README.md
# TODO: add an alarm

formOfAddress = "sir" # your chosen form of address

def speak(text):
    engine.say(text)

def giveWakeUp(text):
    speak(text)
    engine.runAndWait()

def getContactNotifications():
    return getGmailEmails() + " \n\n" + getOffice365Emails()

def giveBriefing():
    text = getGreeting(formOfAddress) + " \n\n" + getDateTime() + " \n\n" + getWeather() + " \n\n" + getEvents() + " \n\n" + getContactNotifications() + " \n\n" + getNews()
    print(text)
    giveWakeUp(text)

giveBriefing()