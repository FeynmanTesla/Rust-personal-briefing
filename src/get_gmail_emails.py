# import sys
# from importlib import reload
# reload(sys)
# sys.setdefaultencoding("utf-8")

import logging

from googleapiclient import errors
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file

# from getEvents import build, errors, Http, file, logging
from process_gmail_message import process_gmail_message

logging.getLogger("googleapicliet.discovery_cache").setLevel(logging.ERROR)

query = "newer_than:3d and is:unread"
maxResultsNo = 10
store = file.Storage("assets/token.json")  # TODO: check whether the token.json file generated ends up here
creds = store.get()
user_id = "me"
formatStr = "full"


def get_gmail_emails():
    service = build("gmail", "v1", http=creds.authorize(Http()))
    try:
        response = service.users().messages().list(userId=user_id, q=query).execute()
        messages = []
        results = ""
        if "messages" in response:
            messages.extend(response["messages"])

        if len(messages) == 0:
            return "You do not have any recent unread G-mail emails."

        for i in range(0, len(messages)):
            results += process_gmail_message(messages[i]["id"], service, errors)
            if i > maxResultsNo - 1:
                break

        results = results[1:len(results)]
        return "Here are your " + str(len(messages)) + " recent unread G-mail emails. " + results
    except errors.HttpError as error:
        print(error)
