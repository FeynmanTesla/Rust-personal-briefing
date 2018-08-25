from getDateTime import datetime, morningAfternoonEveningFromHours

def getGreeting():
    hour = datetime.datetime.now().hour
    morningAfternoonEvening = morningAfternoonEveningFromHours(hour)
    return "Good " + morningAfternoonEvening + " " +  open("formOfAddress.txt","r").read() + "."