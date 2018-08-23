from __future__ import print_function
from googleapiclient.discovery import build
from apiclient import errors

from httplib2 import Http
from oauth2client import file, client, tools

import logging
logging.getLogger("googleapicliet.discovery_cache").setLevel(logging.ERROR)

# If modifying these scopes, delete the file token.json.
SCOPES = "https://www.googleapis.com/auth/calendar.readonly https://www.googleapis.com/auth/gmail.readonly"
#SCOPES = "https://www.googleapis.com/auth/calendar.readonly https://mail.google.com"

# query = "newer_than:3d and is:unread"
# maxResultsNo = 10
# service = build('gmail', 'v1', http=creds.authorize(Http()))
# user_id = "me"

# def getGmailEmails():# TODO: implement this
#     """List all Messages of the user's mailbox matching the query.

#     Args:
#         service: Authorized Gmail API service instance.
#         user_id: User's email address. The special value "me"
#         can be used to indicate the authenticated user.
#         query: String used to filter messages returned.
#         Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

#     Returns:
#         List of Messages that match the criteria of the query. Note that the
#         returned list contains Message IDs, you must use get with the
#         appropriate ID to get the details of a Message.
#     """
#     try:
#         response = service.users().messages().list(userId=user_id, q=query, maxResults=maxResultsNo).execute()
#         messages = []
#         if "messages" in response:
#             messages.extend(response["messages"])

#         while "nextPageToken" in response:
#             page_token = response["nextPageToken"]
#             response = service.users().messages().list(userId=user_id, q=query, maxResults=maxResultsNo, pageToken=page_token).execute()
#             messages.extend(response["messages"])

#         return messages
#     except errors.HttpError, error:
#         print ("An error occurred: %s" % error)

def getGmailEmails():
    return "Gmail emails will go here"