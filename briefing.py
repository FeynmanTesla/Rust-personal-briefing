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

def getGreeting():
    hour = datetime.datetime.now().hour
    morningAfternoonEvening = "morning"
    if (hour >= 12 and hour < 17):
        morningAfternoonEvening = "afternoon"
    if (hour >= 17 and hour < 25):
        morningAfternoonEvening = "evening"
    return "Good " + morningAfternoonEvening + " " + formOfAddress + "."

def getDateTime():
    dateAndTime = datetime.datetime.now()
    dayOfWeek = dateAndTime.strftime("%A")

    month = dateAndTime.strftime("%B")
    dateOfMonth = inflectEngine.ordinal(dateAndTime.strftime("%d"))
    year = inflectEngine.number_to_words(dateAndTime.strftime("%Y"))
    date = dateOfMonth + " of " + month + " " + year

    hours = inflectEngine.number_to_words(dateAndTime.strftime("%I"))
    mins = inflectEngine.number_to_words(dateAndTime.strftime("%M"))
    amPm = dateAndTime.strftime("%p")
    if (amPm == "AM"):
        amPm = "afternoon"
    else:
        amPm = "afternoon"
    time = mins + " past " + hours + " in the " + amPm

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
    print("Getting the upcoming 10 events")
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
    currWeekdayNumber = int(now.strftime("%w")) # Weekday as a number 0-6, 0 is Sunday
    weekdays =  ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    for event in events:
        dateTime = event["start"].get("dateTime", event["start"].get("date")) # format 2018-09-14T17:30:00+01:00 YYYY-MM-DDTHH:MM
        
        year = int(dateTime[0:4])
        monthNumber = int(dateTime[5:7]) - 1
        dayOfMonth = int(dateTime[8:10])
        month = months[monthNumber]
        hours = int(dateTime[11:13])
        mins = int(dateTime[14:16])

        print("\n\n")
        print(year)
        print(monthNumber)
        print(month)
        print(hours)
        print(mins)
        print(event["summary"])

        amPm = "AM"
        if (hours > 12):
            hours -= 12
            amPm = "PM"

        if (year > currYear + 1):
            print("\nbreak 1")
            print(year)
            print(currYear)
            print("break 1\n")
            break
        if (monthNumber > currMonth + 1 or (monthNumber == 0 and currMonth == 11)):
            print("\nbreak 2")
            print(monthNumber)
            print(currMonth)
            print("break 2\n")
            break
        if (monthNumber != currMonth and dayOfMonth > currDayOfMonth):
            print("\nbreak 3")
            print(monthNumber)
            print(currMonth)
            print(dayOfMonth)
            print(currDayOfMonth)
            print("break 3\n")
            break
        
        print("assessing if within a week")
        
        withinAWeek = currMonth == monthNumber and currDayOfMonth + 7 <= dayOfMonth
        if (not withinAWeek): withinAWeek = currMonth != monthNumber and currDayOfMonth + 7 - daysInEachMonth[currMonth] >= dayOfMonth

        print("withinAWeek = " + str(withinAWeek))

        eventsStr += " " + event["summary"] + " is at " + inflectEngine.number_to_words(hours) + " " + inflectEngine.number_to_words(mins) + " " + amPm + " on "
        if (withinAWeek):
            print("within a week")
            diff = dayOfMonth - currDayOfMonth
            if (month != currMonth):
                diff = dayOfMonth + daysInEachMonth[currMonth] - currDayOfMonth #TODO: add leap year compatability
            weekdayNumber = currWeekdayNumber + diff
            eventsStr += weekdays[weekdayNumber]
        eventsStr += " the " + inflectEngine.ordinal(dayOfMonth) + " of " + month + "."

    print(eventsStr)
    if (eventsStr == "Here are your upcoming events for the next month."): eventsStr = "No upcoming events found for the next month."
    return eventsStr


def getContactNotifications():
    return "Contact notifications - emails - will be here."

def main():
    #TODO: add an alarm or something?
    text = getGreeting() + " \n\n" + getDateTime() + " \n\n" + getWeather() + " \n\n" + getEvents() + " \n\n" + getContactNotifications() + " \n\n" + getNews()
    #print(text)
    giveWakeUp(text)

main()