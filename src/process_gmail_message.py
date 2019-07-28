def process_gmail_message(msg_id, service, errors):
    """
    process Gmail emails into a verbose format of sender and subject.
    :param msg_id: a unique identifier to find the email in question.
    :param service: a wrapper module over gmail functionality.
    :param errors: handler library for errors, usually arising from HTTP.
    :return: a verbose format of sender and subject of 1 message.
    """
    try:
        message = service.users().messages().get(userId="me", id=msg_id).execute()
        headers = message["payload"]["headers"]

        emailFrom = ""
        subject = ""

        for i in range(len(headers)):
            if emailFrom != "" and subject != "":
                break
            header = headers[i]
            if header["name"] == "From":
                emailFrom = header["value"].replace("\"", "")
                emailFrom = emailFrom[:emailFrom.find("<")]
                if emailFrom[len(emailFrom) - 1] != " ":
                    emailFrom += " "
            elif header["name"] == "Subject":
                subject = header["value"]
                lastChar = subject[len(subject) - 1]
                if lastChar != "!" and lastChar != "." and lastChar != "?":
                    subject += "."

        if emailFrom != "" and subject != "":
            return " " + emailFrom + "sent you an email about " + subject
        else:
            return ""
    except errors.HttpError as error:
        print(error)
