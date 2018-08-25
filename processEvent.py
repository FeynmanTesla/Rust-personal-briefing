
from getDateTime import timeToSpoken, inflectEngine

def processEvent(event, currYear, currMonth, currDayOfMonth, months, daysInEachMonth, currWeekdayNumber, weekdays):
    result = ""
    dateTime = event["start"].get("dateTime", event["start"].get("date")) # format 2018-09-14T17:30:00+01:00 YYYY-MM-DDTHH:MM
    
    year = int(dateTime[0:4])
    monthNumber = int(dateTime[5:7]) - 1
    dayOfMonth = int(dateTime[8:10])
    month = months[monthNumber]
    hours = int(dateTime[11:13])
    mins = int(dateTime[14:16])

    if (year > currYear + 1): return "break"
    if (monthNumber != currMonth and monthNumber != currMonth + 1): return "break"
    if (monthNumber == currMonth + 1 and dayOfMonth > currDayOfMonth + 3): return "break"
    
    withinAWeek = currMonth == monthNumber and currDayOfMonth + 7 >= dayOfMonth
    if (not withinAWeek): withinAWeek = currMonth != monthNumber and currDayOfMonth + 7 - daysInEachMonth[currMonth] >= dayOfMonth

    result += " " + event["summary"] + " is at " + timeToSpoken(hours, mins)
    if (withinAWeek):
        diff = dayOfMonth - currDayOfMonth
        if (monthNumber != currMonth):
            diff = dayOfMonth + daysInEachMonth[currMonth] - currDayOfMonth
            if (currMonth == 1):
                leapYear = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
                if (leapYear): diff += 1
        weekdayNumber = (currWeekdayNumber + diff) % 7
        if (diff == 0): result += " today."
        else: result += " on " + weekdays[weekdayNumber] + ", the " + inflectEngine.ordinal(dayOfMonth) + " of " + month + "."
    else: result += " on the " + inflectEngine.ordinal(dayOfMonth) + " of " + month + "."
    return result