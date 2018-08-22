import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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
    return "Events from Calendar will be here."

def getContactNotifications():
    return "Contact notifications - emails - will be here."

def main():
    #TODO: add an alarm or something?
    text = getGreeting() + " \n\n" + getDateTime() + " \n\n" + getWeather() + " \n\n" + getEvents() + " \n\n" + getContactNotifications() + " \n\n" + getNews()
    print(text)
    giveWakeUp(text)

main()