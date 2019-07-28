from datetime import date, datetime

import inflect
import requests
from pyowm import OWM

current_day_of_month = int(date.today().day)
city_id = int(open("../conf/city_id.txt", "r").read())
city_name = open("../conf/city_name.txt", "r").read()
owm_api_key = open("../conf/owm_api_key.txt", "r").read()

inflectEngine = inflect.engine()

owm = OWM(owm_api_key, language="en")
current_weather = owm.weather_at_id(city_id).get_weather()

forecast_url = "https://api.openweathermap.org/data/2.5/forecast?id=" + str(city_id) + "&appid=" + owm_api_key + \
               "&units=metric&lang=en"
forecast_data = requests.get(url=forecast_url)


def get_forecast():
    """
    get the weather for the rest of the current day in a verbose format.
    """
    fcast_items = forecast_data.json()["list"]
    min_fcast_temp = 100
    max_fcast_temp = -100
    all_fcast_conditions = []

    for fcast_item in fcast_items:
        day_date_time = int(datetime.strptime(fcast_item["dt_txt"], "%Y-%m-%d %H:%M:%S").day)
        if day_date_time > current_day_of_month:
            break
        local_min_temp = fcast_item["main"]["temp_min"]
        local_max_temp = fcast_item["main"]["temp_max"]
        if local_max_temp > max_fcast_temp:
            max_fcast_temp = local_max_temp
        if local_min_temp < min_fcast_temp:
            min_fcast_temp = local_min_temp
        day_conditions = fcast_item["weather"][0]["description"]
        if not all_fcast_conditions.__contains__(day_conditions):
            all_fcast_conditions.append(day_conditions)

    all_fcast_conditions_str = ""
    i = 0
    while i < len(all_fcast_conditions):
        if i == 0:
            all_fcast_conditions_str += str(all_fcast_conditions[i])
        elif i == len(all_fcast_conditions) - 1:
            all_fcast_conditions_str += ", and " + str(all_fcast_conditions[i])
        else:
            all_fcast_conditions_str += str(all_fcast_conditions[i])
        i += 1

    min_fcast_temp = int(round(float(min_fcast_temp)))
    max_fcast_temp = int(round(float(max_fcast_temp)))

    if min_fcast_temp == 100 and max_fcast_temp == -100:
        return ""

    else:
        return "The forecasted conditions for the rest of the day are " + all_fcast_conditions_str +\
               " with highs of " + str(max_fcast_temp) + " and lows of " + str(min_fcast_temp) + " degrees celsius."


def get_weather():
    """
    get the current weather and the forecasted conditions for the rest of the day.
    """
    current_conditions = current_weather.get_detailed_status()
    current_temp = inflectEngine.number_to_words(
        int(round(float(current_weather.get_temperature(unit='celsius')["temp"]))))

    return "The current conditions in " + city_name + " are " + current_conditions + \
           " with a current temperature of " + str(current_temp) + " degrees celsius." + " " + get_forecast()
