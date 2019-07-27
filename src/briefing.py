# import sys
# from importlib import reload
# reload(sys)
# sys.setdefaultencoding("utf-8")

from getGmailEmails import get_gmail_emails
from getNews import get_news
from getGreeting import get_greeting
from getWeather import getWeather
from getDateTime import get_date_time, datetime
from getEvents import get_events
from getOffice365Emails import get_office_365_emails

import pyttsx3

engine = pyttsx.init()


# TODO: add error handling

def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_contact_notifications():
    return get_gmail_emails() + " \n\n" + get_office_365_emails()


def give_briefing():
    text = get_greeting() + " \n\n" + get_date_time() + " \n\n" + getWeather() + " \n\n" + get_events() + " \n\n" + \
           get_contact_notifications() + " \n\n" + get_news()
    # text = get_greeting() + " \n\n" + get_date_time() + " \n\n" + " \n\n" + getEvents() + \
    #     " \n\n" + get_contact_notifications() + " \n\n" + get_news()
    speak(text)


give_briefing()  # TODO: remove post-debugging
