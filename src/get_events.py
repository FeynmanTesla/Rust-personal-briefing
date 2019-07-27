from __future__ import print_function

import logging

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

from get_date_time import datetime
from process_event import process_event

logging.getLogger("googleapicliet.discovery_cache").setLevel(logging.ERROR)

now = datetime.datetime.now()
currYear = int(now.strftime("%Y"))
currMonth = int(now.strftime("%m")) - 1
currDayOfMonth = int(now.strftime("%d"))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]
daysInEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

currWeekdayNumber = int(now.strftime("%w")) - 1
# Weekday as a number 0-6, 0 is Monday with -1 and if =-1 then 6 adjustment

if currWeekdayNumber == -1:
    currWeekdayNumber = 6
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# If modifying these scopes, delete the file token.json.
SCOPES = "https://www.googleapis.com/auth/calendar.readonly https://www.googleapis.com/auth/gmail.readonly"


def get_events():
    store = file.Storage("assets/token.json")  # TODO: check whether the token.json file generated ends up here
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets("assets/credentials.json", SCOPES)
        creds = tools.run_flow(flow, store)
    service = build("calendar", "v3", http=creds.authorize(Http()))

    # Call the Calendar API
    now_local_scope = datetime.datetime.utcnow().isoformat() + "Z"  # "Z" indicates UTC time
    events_result = service.events().list(calendarId="primary", timeMin=now_local_scope, maxResults=10,
                                          singleEvents=True, orderBy="startTime").execute()
    events = events_result.get("items", [])

    if not events:
        return "No upcoming events found for the next month."
    eventsStr = "Here are your upcoming events for the next month."

    for event in events:
        result = process_event(event, currYear, currMonth, currDayOfMonth, months, daysInEachMonth, currWeekdayNumber,
                               weekdays)
        if result == "break":
            break
        else:
            eventsStr += result

    if eventsStr == "Here are your upcoming events for the next month.":
        eventsStr = "No upcoming events found for the next month."
    return eventsStr
