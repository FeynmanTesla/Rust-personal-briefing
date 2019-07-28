from get_date_time import time_to_spoken, inflectEngine


def process_event(event, curr_year, curr_month, curr_day_of_month, months, days_in_each_month,
                  curr_weekday_number, weekdays):
    """
    :param event: an instance of a module in the Google Calendar API abstracting events.
    :param curr_year: the current year.
    :param curr_month: the current month.
    :param curr_day_of_month: the current date, i.e. day in the month, e.g. 23rd.
    :param months: an array containing the months of the year as strings.
    :param days_in_each_month: an array containing the number of days in each month of the year.
    :param curr_weekday_number: an integer representation of the current day of the week.
    :param weekdays: an array containing the days of the week as strings.
    :return: a verbose summary of an event based on its data.
    """
    result = ""
    dateTime = event["start"].get("dateTime",
                                  event["start"].get("date"))  # format 2018-09-14T17:30:00+01:00 YYYY-MM-DDTHH:MM

    year = int(dateTime[0:4])
    monthNumber = int(dateTime[5:7]) - 1
    dayOfMonth = int(dateTime[8:10])
    month = months[monthNumber]

    # time might not be given, e.g. if all day
    timeGiven = len(dateTime) > 10  # deal with it later as appending to result

    if year > curr_year + 1:
        return "break"
    if monthNumber != curr_month and monthNumber != curr_month + 1:
        return "break"
    if monthNumber == curr_month + 1 and dayOfMonth > curr_day_of_month + 3:
        return "break"

    withinAWeek = curr_month == monthNumber and curr_day_of_month + 7 >= dayOfMonth
    if not withinAWeek:
        withinAWeek = curr_month != monthNumber and curr_day_of_month + 7 - days_in_each_month[curr_month] >= dayOfMonth

    result += " " + event["summary"]

    if timeGiven:
        hours = int(dateTime[11:13])
        mins = int(dateTime[14:16])
        result += " is at " + time_to_spoken(hours, mins)

    if withinAWeek:
        diff = dayOfMonth - curr_day_of_month
        if monthNumber != curr_month:
            diff = dayOfMonth + days_in_each_month[curr_month] - curr_day_of_month
            if curr_month == 1:
                leapYear = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
                if leapYear:
                    diff += 1
        weekdayNumber = (curr_weekday_number + diff) % 7
        if diff == 0:
            result += " today."
        else:
            result += " on " + weekdays[weekdayNumber] + ", the " + inflectEngine.ordinal(
                dayOfMonth) + " of " + month + "."
    else:
        result += " on the " + inflectEngine.ordinal(dayOfMonth) + " of " + month + "."
    return result
