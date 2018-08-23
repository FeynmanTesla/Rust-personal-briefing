from getEvents import print_function, build, errors, Http, file, client, tools, logging, SCOPES
logging.getLogger("googleapicliet.discovery_cache").setLevel(logging.ERROR)

query = "newer_than:3d and is:unread"
maxResultsNo = 10
store = file.Storage("token.json")
creds = store.get()
service = build("gmail", "v1", http=creds.authorize(Http()))
user_id = "me"
formatStr = "full"

def getGmailEmails():
    """List all Messages of the user's mailbox matching the query.

    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        query: String used to filter messages returned.
        Eg.- "from:user@some_domain.com" for Messages from a particular sender.

    Returns:
        List of Messages that match the criteria of the query. Note that the
        returned list contains Message IDs, you must use get with the
        appropriate ID to get the details of a Message.
    """
    try:
        response = service.users().messages().list(userId=user_id,maxResults=maxResultsNo,q=query).execute()
        messages = []
        if "messages" in response:
            messages.extend(response["messages"])

        while "nextPageToken" in response:
            page_token = response["nextPageToken"]
            response = service.users().messages().list(userId=user_id,maxResults=maxResultsNo,q=query).execute()
            messages.extend(response["messages"])
        
        return messages
    except errors.HttpError, error:
        return "An error occurred: %s" % error

def messageJSONToString(messageJSON):
    headers = messageJSON["payload"]["headers"]
    return " " + headers["From"] + " sent you an email about " + headers["Subject"] + "."

#print(getGmailEmails())
print(getGmailEmails())

def ListMessagesMatchingQuery():
    try:
        response = service.users().messages().list(userId=user_id,q=query).execute()
        messages = []
        results = ""
        if "messages" in response:
            messages.extend(response["messages"])
        for i in range(0, len(messages) - 1):
            if (i == len(messages) - 1): results += ", and "
            elif (i != 0): results += ", "
            results = results + ", " + GetMessage(messages[i]["id"])
            if(i > maxResultsNo - 1): break
        
        results = results[1:len(results)]

        if(v==0):
            return "You do not have any unread emails."
        else:
            return "You have unread emails from " + results
    except errors.HttpError, error:
        print (error)

def GetMessage(msg_id):
    try:
        message = service.users().messages().get(userId="me", id=msg_id).execute()
        details = message["payload"]
        headers = details["headers"]

        #print(headers)
        
        email_from = headers["From"]
        email_from = email_from.replace("\"", "")
        email_from = email_from[:email_from.find("<")]

        subject = headers["Subject"].replace("\"", "")

        return email_from + " sent you an email about " + subject + "."
    except errors.HttpError, error:
        print (error)

print("\n\n\n\n\n\n")
print("Now for the decent solution")
print(ListMessagesMatchingQuery())