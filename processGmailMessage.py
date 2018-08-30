def processGmailMessage(msg_id, service, errors):
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
                if (emailFrom[len(emailFrom) - 1] != " "): emailFrom += " "
            elif(header["name"] == "Subject"):
                subject = header["value"]
                lastChar = subject[len(subject) - 1]
                if (lastChar != "!" and lastChar != "." and lastChar != "?"): subject += "."
            
        if (emailFrom != "" and subject != ""): return " " + emailFrom + "sent you an email about " + subject
        else: return ""
    except error:
        print (error)