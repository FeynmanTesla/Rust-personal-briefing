from getDateTime import datetime, morning_afternoon_or_evening_from_hours


def get_greeting():
    hour = datetime.datetime.now().hour
    morning_afternoon_evening = morning_afternoon_or_evening_from_hours(hour)
    return "Good " + morning_afternoon_evening + " " + open("conf/formOfAddress.txt", "r").read() + "."
