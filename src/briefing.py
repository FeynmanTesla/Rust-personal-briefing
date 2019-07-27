import pyttsx3
from get_date_time import get_date_time
from get_events import get_events
from get_gmail_emails import get_gmail_emails
from get_greeting import get_greeting
from get_news import get_news
from get_office_365_emails import get_office_365_emails
from get_weather import get_weather

engine = pyttsx3.init()


# TODO: add error handling

def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_contact_notifications():
    return get_gmail_emails() + " \n\n" + get_office_365_emails()


def get_briefing_text():
    text = get_greeting() + " \n\n" + get_date_time() + " \n\n" + get_weather() + " \n\n" + get_events() + " \n\n" + \
           get_contact_notifications() + " \n\n" + get_news()
    return text


def give_briefing():
    text = get_briefing_text()
    print(text)
    speak(text)

give_briefing()
