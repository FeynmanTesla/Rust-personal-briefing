from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)
import datetime

woeid = int(open("woeid.txt","r").read()) # this is the ID for your city from Yahoo's Weather API. By default, St Andrews, Scotland.
# Learn how to find your city's woeid here: https://developer.yahoo.com/weather/documentation.html
cityName = open("cityName.txt","r").read() # the name of your city.

import inflect
inflectEngine = inflect.engine()

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