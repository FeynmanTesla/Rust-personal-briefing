import datetime

import inflect

inflectEngine = inflect.engine()


def morning_afternoon_or_evening_from_hours(hours):
    """
    :param hours: the current hour of the day.
    :return: return whether it is morning, afternoon, or evening, based on the time.
    """
    result = "morning"
    if 12 <= hours < 17:
        result = "afternoon"
    if 17 <= hours < 25:
        result = "evening"
    return result


def time_to_spoken(hours, mins):
    """
    :param hours: the current hour of the day.
    :param mins: the minutes passed in the current hour.
    :return: a verbose form of the current time.
    """
    nearerFloorHour = True
    mins = int(5 * round(float(mins) / 5))  # round to nearest 5

    if mins == 60:
        hours += 1
        mins = 0

    morningAfternoonEvening = morning_afternoon_or_evening_from_hours(hours)

    if mins > 30:
        hours += 1
        if hours == 25:
            hours = 1
        mins = 60 - mins
        nearerFloorHour = False
    if hours > 12:
        hours -= 12

    hours = inflectEngine.number_to_words(hours)
    minsStr = inflectEngine.number_to_words(mins)
    if minsStr == "fifteen":
        minsStr = "quarter"
    if mins == 30:
        minsStr = "half"

    if mins == 0:
        return hours + " o'clock in the " + morningAfternoonEvening
    elif nearerFloorHour:
        return minsStr + " past " + hours + " in the " + morningAfternoonEvening
    else:
        return minsStr + " to " + hours + " in the " + morningAfternoonEvening


def get_date_time():
    """
    :return: a verbose description of the current date and time.
    """
    dateAndTime = datetime.datetime.now()
    dayOfWeek = dateAndTime.strftime("%A")

    month = dateAndTime.strftime("%B")
    dateOfMonth = inflectEngine.ordinal(dateAndTime.strftime("%d"))
    year = inflectEngine.number_to_words(dateAndTime.strftime("%Y"))
    date = dateOfMonth + " of " + month + ", " + year

    hour = int(dateAndTime.strftime("%H"))
    mins = int(dateAndTime.strftime("%M"))
    time = time_to_spoken(hour, mins)

    return "It is " + time + " of " + dayOfWeek + ", the " + date + "."
