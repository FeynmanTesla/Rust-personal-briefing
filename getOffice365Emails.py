from O365 import *
import json
import os
import sys
import time
import logging

office365EmailAddress = open("office365EmailAddress.txt","r").read()
office365EmailPassword = open("office365EmailPassword.txt","r").read()

def processMessage(m):
    sender = str(m.getSender()["EmailAddress"]["Name"])
    subject = str(m.getSubject())
    lastChar = subject[len(subject) - 1]
    if (lastChar != "!" and lastChar != "." and lastChar != "?"): subject += "."
    return " " + sender + " sent you an email about " + subject

def getOffice365Emails():
    auth = (office365EmailAddress,office365EmailPassword)
    inbox = Inbox(auth, getNow=False) #Email, Password, Delay fetching so I can change the filters.
    inbox.setFilter("IsRead eq false")

    if (inbox.getMessages() == False): return "Sorry, I was unable to retrieve your Office three six five emails."

    messages = inbox.messages
    number = len(messages)

    if (number == 0): return "You have no recent unread Office three six five emails."

    result = "Here are your " + str(number) + " recent unread Office three six five emails."

    i = 1
    for m in inbox.messages:
        if (i == 10): break
        result += processMessage(m)
        i += 1
    
    return result

print(getOffice365Emails())