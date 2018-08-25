import datetime
import inflect
inflectEngine = inflect.engine()

def morningAfternoonEveningFromHours(hours):
    result = "morning"
    if (hours >= 12 and hours < 17):
        result = "afternoon"
    if (hours >= 17 and hours < 25):
        result = "evening"
    return result

def timeToSpoken(hours, mins):
    nearerFloorHour = True
    mins = int(5 * round(float(mins)/5)) # round to nearest 5
    if (mins == 60):
        hours += 1
        mins = 0
    morningAfternoonEvening = morningAfternoonEveningFromHours(hours)
    if (mins > 30):
        hours += 1
        if (hours == 25): hours = 1
        mins = 60 - mins
        nearerFloorHour = False
    if (hours > 12): hours -= 12
    hours = inflectEngine.number_to_words(hours)
    minsStr = inflectEngine.number_to_words(mins)
    if (minsStr == "fifteen"): minsStr = "quarter"
    if (mins == 30): minsStr = "half"
    
    if (mins == 0): return hours + "o'clock in the " + morningAfternoonEvening
    if (nearerFloorHour): return minsStr +  " past " + hours + " in the " + morningAfternoonEvening
    return minsStr +  " to " + hours + " in the " + morningAfternoonEvening

def getDateTime():
    dateAndTime = datetime.datetime.now()
    dayOfWeek = dateAndTime.strftime("%A")

    month = dateAndTime.strftime("%B")
    dateOfMonth = inflectEngine.ordinal(dateAndTime.strftime("%d"))
    year = inflectEngine.number_to_words(dateAndTime.strftime("%Y"))
    date = dateOfMonth + " of " + month + ", " + year

    hour = int(dateAndTime.strftime("%H"))
    mins = int(dateAndTime.strftime("%M"))
    time = timeToSpoken(hour, mins)

    return "It is " + time + " of " + dayOfWeek + ", the " + date + "."