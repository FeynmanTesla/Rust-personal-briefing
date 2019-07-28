from get_date_time import datetime, morning_afternoon_or_evening_from_hours


def get_greeting():
    """
    :return: a verbose greeting based on the current time and user's preferred form of address.
    """
    hour = datetime.datetime.now().hour
    morning_afternoon_evening = morning_afternoon_or_evening_from_hours(hour)
    return "Good " + morning_afternoon_evening + " " + open("../conf/form_of_address.txt", "r").read() + "."
