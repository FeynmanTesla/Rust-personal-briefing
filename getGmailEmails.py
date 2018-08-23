import sys
reload(sys)
sys.setdefaultencoding("utf-8")

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
    try:
        response = service.users().messages().list(userId=user_id,q=query).execute()
        messages = []
        results = ""
        if "messages" in response: messages.extend(response["messages"])
        
        if (len(messages) == 0): return "You do not have any recent unread G-mail emails."

        for i in range(0, len(messages) - 1):
            results += getMessage(messages[i]["id"])
            if(i > maxResultsNo - 1): break
        
        results = results[1:len(results)]
        return "Here are your recent unread G-mail emails. " + results
    except errors.HttpError, error:
        print (error)

def getMessage(msg_id):
    try:
        message = service.users().messages().get(userId="me", id=msg_id).execute()
        headers = message["payload"]["headers"]
        
        emailFrom = ""
        subject = ""

        for i in range(len(headers)):
            if (emailFrom != "" and subject != ""): break
            header = headers[i]
            if(header["name"] == "From"):
                emailFrom = header["value"].replace("\"", "")
                emailFrom = emailFrom[:emailFrom.find("<")]
            elif(header["name"] == "Subject"):
                subject = header["value"]
            
        if (emailFrom != "" and subject != ""): return " " + emailFrom + "sent you an email about " + subject + "."
        else: return ""
    except errors.HttpError, error:
        print (error)