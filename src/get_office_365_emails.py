from O365 import *
# import json
# import os
# import sys
# import time
# import logging

office365EmailAddress = open("../conf/office365EmailAddress.txt", "r").read()
office365EmailPassword = open("../conf/office365EmailPassword.txt", "r").read()


def process_message(m):
    sender = str(m.getSender()["EmailAddress"]["Name"])
    subject = str(m.getSubject())
    last_char = subject[len(subject) - 1]
    if last_char != "!" and last_char != "." and last_char != "?":
        subject += "."
    return " " + sender + " sent you an email about " + subject


def get_office_365_emails():
    auth = (office365EmailAddress, office365EmailPassword)
    inbox = Inbox(auth, getNow=False)  # Email, Password, Delay fetching so I can change the filters.
    inbox.setFilter("IsRead eq false")

    if not inbox.getMessages():
        return "Sorry, I was unable to retrieve your Office three six five emails."

    messages = inbox.messages
    number = len(messages)

    if number == 0:
        return "You have no recent unread Office three six five emails."

    result = "Here are your " + str(number) + " recent unread Office three six five emails."

    i = 1
    for m in inbox.messages:
        if i == 10:
            break
        result += process_message(m)
        i += 1

    return result
