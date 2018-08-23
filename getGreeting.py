from getDateTime import datetime, morningAfternoonEveningFromHours

def getGreeting(formOfAddress):
    hour = datetime.datetime.now().hour
    morningAfternoonEvening = morningAfternoonEveningFromHours(hour)
    return "Good " + morningAfternoonEvening + " " + formOfAddress + "."