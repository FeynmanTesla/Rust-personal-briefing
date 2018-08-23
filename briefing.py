from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import logging

logging.getLogger("googleapicliet.discovery_cache").setLevel(logging.ERROR)

# If modifying these scopes, delete the file token.json.
SCOPES = "https://www.googleapis.com/auth/calendar.readonly"

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pyttsx
engine = pyttsx.init()

from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)
import datetime

import inflect
inflectEngine = inflect.engine()

from newsapi import NewsApiClient

# TODO: clean up code, shard and abstract functions, split into multiple classes (and files <= 50 lines each)
# TODO: add error handling


# CONFIGURATION

formOfAddress = "sir" # your chosen form of address

woeid = 35567 # this is the ID for your city from Yahoo's Weather API. By default, St Andrews, Scotland.
# Learn how to find your city's woeid here: https://developer.yahoo.com/weather/documentation.html
cityName = "St Andrews" # the name of your city.

newsApiOrgApiKey = open("newsApiOrgAPIKey.txt","r").read() # a text file containing your free API key from https://newsapi.org/
newsApiOrgSources = "the-guardian-uk,bbc-news,al-jazeera-english,independent" # the news sources the headlines are from
# format of sources: comma-separated string of source ids. See sources at: https://newsapi.org/docs/endpoints/sources

def speak(text):
    engine.say(text)

def giveWakeUp(text):
    speak(text)
    engine.runAndWait()

def getWeather():
    lookup = weather.lookup(woeid)
    condition = lookup.condition

    currentConditions = condition.text.lower()
    currentTemp = inflectEngine.number_to_words(condition.temp)
    currentWeather = "The current conditions in " + cityName + " are " + currentConditions + " with a current temperature of " + currentTemp + " degrees celsius."

    todaysForecast = (lookup.forecast)[0]
    forecastedConditions = todaysForecast.text.lower()
    highs = inflectEngine.number_to_words(todaysForecast.high)
    lows = inflectEngine.number_to_words(todaysForecast.low)
    forecastedWeather = "Today's forecasted conditions are " + forecastedConditions + " with highs of " + highs + " and lows of " + lows + " degrees celsius."

    return currentWeather + " " + forecastedWeather

def timeToSpoken(hours, mins):
    nearerFloorHour = True
    if (mins > 30):
        hours += 1
        if (hours == 25): hours = 1
        mins = 60 - mins
        nearerFloorHour = False
    
    morningAfternoonEvening = morningAfternoonEveningFromHours(hours)
    if (hours > 12): hours -= 12
    hours = inflectEngine.number_to_words(hours)
    minsStr = inflectEngine.number_to_words(mins)
    if (minsStr == "fifteen"): minsStr = "quarter"
    if (mins == 30): minsStr = "half"
    
    if (nearerFloorHour):
        if (mins == 0): minsStr = "o'clock"
        return minsStr +  " past " + hours + " in the " + morningAfternoonEvening
    return minsStr +  " to " + hours + " in the " + morningAfternoonEvening

def morningAfternoonEveningFromHours(hours):
    result = "morning"
    if (hours >= 12 and hours < 17):
        result = "afternoon"
    if (hours >= 17 and hours < 25):
        result = "evening"
    return result

def getGreeting():
    hour = datetime.datetime.now().hour
    morningAfternoonEvening = morningAfternoonEveningFromHours(hour)
    return "Good " + morningAfternoonEvening + " " + formOfAddress + "."

def getDateTime():
    dateAndTime = datetime.datetime.now()
    dayOfWeek = dateAndTime.strftime("%A")

    month = dateAndTime.strftime("%B")
    dateOfMonth = inflectEngine.ordinal(dateAndTime.strftime("%d"))
    year = inflectEngine.number_to_words(dateAndTime.strftime("%Y"))
    date = dateOfMonth + " of " + month + " " + year

    hour = int(dateAndTime.strftime("%I"))
    mins = int(dateAndTime.strftime("%M"))
    time = timeToSpoken(hour, mins)

    return "It is " + time + " of " + dayOfWeek + ", the " + date + "."

def getNews():
    newsapi = NewsApiClient(api_key=newsApiOrgApiKey)
    top_headlines = newsapi.get_top_headlines(sources=newsApiOrgSources)
    if (top_headlines["status"] != "ok"): return "I was unable to retrieve news headlines."

    articles = top_headlines["articles"]
    headlines = "Here are the news headlines."
    for article in articles:
        headlines += " " + article["title"]
        finalHeadlineChar = article["title"][len(article["title"]) - 1]
        if (finalHeadlineChar != "!" and finalHeadlineChar != "." and finalHeadlineChar != "?" and finalHeadlineChar != ";"): headlines += "."
    return headlines

def getEvents():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    
    store = file.Storage("token.json")
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
        creds = tools.run_flow(flow, store)
    service = build("calendar", "v3", http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z" # "Z" indicates UTC time
    events_result = service.events().list(calendarId="primary", timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy="startTime").execute()
    events = events_result.get("items", [])

    if not events:
         return "No upcoming events found for the next month."
    eventsStr = "Here are your upcoming events for the next month."
    now = datetime.datetime.now()

    currYear = int(now.strftime("%Y"))
    currMonth = int(now.strftime("%m")) - 1
    currDayOfMonth = int(now.strftime("%d"))
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    daysInEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    currWeekdayNumber = int(now.strftime("%w")) - 1 # Weekday as a number 0-6, 0 is Monday with -1 and if =-1 then 6 adjustment
    if (currWeekdayNumber == -1): currWeekdayNumber = 6
    weekdays =  ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for event in events:
        dateTime = event["start"].get("dateTime", event["start"].get("date")) # format 2018-09-14T17:30:00+01:00 YYYY-MM-DDTHH:MM
        
        year = int(dateTime[0:4])
        monthNumber = int(dateTime[5:7]) - 1
        dayOfMonth = int(dateTime[8:10])
        month = months[monthNumber]
        hours = int(dateTime[11:13])
        mins = int(dateTime[14:16])

        if (year > currYear + 1): break
        if (monthNumber != currMonth and monthNumber != currMonth + 1): break
        if (monthNumber == currMonth + 1 and dayOfMonth > currDayOfMonth + 3): break
        
        withinAWeek = currMonth == monthNumber and currDayOfMonth + 7 >= dayOfMonth
        if (not withinAWeek): withinAWeek = currMonth != monthNumber and currDayOfMonth + 7 - daysInEachMonth[currMonth] >= dayOfMonth

        eventsStr += " " + event["summary"] + " is at " + timeToSpoken(hours, mins)
        if (withinAWeek):
            diff = dayOfMonth - currDayOfMonth
            if (monthNumber != currMonth):
                diff = dayOfMonth + daysInEachMonth[currMonth] - currDayOfMonth
                if (currMonth == 1):
                    leapYear = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
                    if (leapYear): diff += 1
            weekdayNumber = (currWeekdayNumber + diff) % 7
            if (diff == 0):
                eventsStr += " today."
                continue
            else:
                eventsStr += " on " + weekdays[weekdayNumber] + ", the " + inflectEngine.ordinal(dayOfMonth) + " of " + month + "."
                continue
        else: eventsStr += " on the " + inflectEngine.ordinal(dayOfMonth) + " of " + month + "."

    if (eventsStr == "Here are your upcoming events for the next month."): eventsStr = "No upcoming events found for the next month."
    return eventsStr

def getGmailEmails():# TODO: implement this
    return "The number of new unread G mail emails here, then the title and sender of each email."

def getOffice365Emails():# TODO: implement this
    return "The number of new unread office 365 emails here, then the title and sender of each email."

def getContactNotifications():
    return getGmailEmails() + " \n\n" + getOffice365Emails()

def main():
    #TODO: add an alarm or something?
    text = getGreeting() + " \n\n" + getDateTime() + " \n\n" + getWeather() + " \n\n" + getEvents() + " \n\n" + getContactNotifications() + " \n\n" + getNews()
    print(text)
    giveWakeUp(text)

main()