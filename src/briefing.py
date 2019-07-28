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
    """
    use the pyttsx3 package's TTS engine to read out a string.
    :param text: the string to read.
    """
    engine.say(text)
    engine.runAndWait()


def get_contact_notifications():
    """
    use the associated modules to get recent unread emails in a verbose format.
    """
    return get_gmail_emails() + " \n\n" + get_office_365_emails()


def get_briefing_text():
    """
    :return: a verbose briefing built up from functions from related modules.
    """
    text = get_greeting() + " \n\n" + get_date_time() + " \n\n" + get_weather() + " \n\n" + get_events() + " \n\n" + \
           get_contact_notifications() + " \n\n" + get_news()
    return text


def give_briefing():
    """
    get a briefing from the get_briefing_text() method and use pyttsx3 to say it as well as printing it to the user.
    """
    text = get_briefing_text()
    print(text)
    speak(text)
