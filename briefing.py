# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

import pyttsx3
engine = pyttsx3.init()

from getGmailEmails import getGmailEmails
from getNews import getNews
from getGreeting import getGreeting
from getWeather import getWeather
from getDateTime import getDateTime, datetime
from getEvents import getEvents
from getOffice365Emails import getOffice365Emails

# TODO: add error handling

def speak(text):
    engine.say(text)
    engine.runAndWait()

def getContactNotifications():
    return getGmailEmails() + " \n\n" + getOffice365Emails()

def giveBriefing():
    text = getGreeting() + " \n\n" + getDateTime() + " \n\n" + getWeather() + " \n\n" + getEvents() + " \n\n" + getContactNotifications() + " \n\n" + getNews()
    speak(text)