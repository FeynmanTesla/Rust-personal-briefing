from __future__ import print_function
from googleapiclient.discovery import build

from apiclient import errors

from httplib2 import Http
from oauth2client import file, client, tools

import logging

logging.getLogger("googleapicliet.discovery_cache").setLevel(logging.ERROR)

from getDateTime import datetime, timeToSpoken, inflectEngine

# If modifying these scopes, delete the file token.json.
SCOPES = "https://www.googleapis.com/auth/calendar.readonly https://www.googleapis.com/auth/gmail.readonly"

def getEvents():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    
    store = file.Storage("token.json")
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
        creds = tools.run_flow(flow, store)
    service = build("calendar", "v3", http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z" # "Z" indicates UTC time
    events_result = service.events().list(calendarId="primary", timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy="startTime").execute()
    events = events_result.get("items", [])

    if not events:
         return "No upcoming events found for the next month."
    eventsStr = "Here are your upcoming events for the next month."
    now = datetime.datetime.now()

    currYear = int(now.strftime("%Y"))
    currMonth = int(now.strftime("%m")) - 1
    currDayOfMonth = int(now.strftime("%d"))
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    daysInEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    currWeekdayNumber = int(now.strftime("%w")) - 1 # Weekday as a number 0-6, 0 is Monday with -1 and if =-1 then 6 adjustment
    if (currWeekdayNumber == -1): currWeekdayNumber = 6
    weekdays =  ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for event in events:
        dateTime = event["start"].get("dateTime", event["start"].get("date")) # format 2018-09-14T17:30:00+01:00 YYYY-MM-DDTHH:MM
        
        year = int(dateTime[0:4])
        monthNumber = int(dateTime[5:7]) - 1
        dayOfMonth = int(dateTime[8:10])
        month = months[monthNumber]
        hours = int(dateTime[11:13])
        mins = int(dateTime[14:16])

        if (year > currYear + 1): break
        if (monthNumber != currMonth and monthNumber != currMonth + 1): break
        if (monthNumber == currMonth + 1 and dayOfMonth > currDayOfMonth + 3): break
        
        withinAWeek = currMonth == monthNumber and currDayOfMonth + 7 >= dayOfMonth
        if (not withinAWeek): withinAWeek = currMonth != monthNumber and currDayOfMonth + 7 - daysInEachMonth[currMonth] >= dayOfMonth

        eventsStr += " " + event["summary"] + " is at " + timeToSpoken(hours, mins)
        if (withinAWeek):
            diff = dayOfMonth - currDayOfMonth
            if (monthNumber != currMonth):
                diff = dayOfMonth + daysInEachMonth[currMonth] - currDayOfMonth
                if (currMonth == 1):
                    leapYear = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
                    if (leapYear): diff += 1
            weekdayNumber = (currWeekdayNumber + diff) % 7
            if (diff == 0):
                eventsStr += " today."
                continue
            else:
                eventsStr += " on " + weekdays[weekdayNumber] + ", the " + inflectEngine.ordinal(dayOfMonth) + " of " + month + "."
                continue
        else: eventsStr += " on the " + inflectEngine.ordinal(dayOfMonth) + " of " + month + "."

    if (eventsStr == "Here are your upcoming events for the next month."): eventsStr = "No upcoming events found for the next month."
    return eventsStr