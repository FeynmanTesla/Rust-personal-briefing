from O365 import Account
required_scopes = ['basic', 'mailbox']

client_id = open("../conf/office_365_client_id.txt", "r").read()
client_secret = open("../conf/office_365_client_secret.txt", "r").read()


def process_message(m):
    sender = str(str(m.sender).split(" (")[0])
    subject = str(m.subject)
    last_char = subject[len(subject) - 1]
    if last_char != "!" and last_char != "." and last_char != "?":
        subject += "."
    return " " + sender + " sent you an email about " + subject


def get_office_365_emails():
    account = Account((client_id, client_secret))

    if not account.is_authenticated:  # if an existing, unexpired access token doesn't exist then get one
        account.authenticate(scopes=required_scopes)

    mailbox = account.mailbox()
    messages = mailbox.get_messages(limit=10, query="IsRead eq false")
    result = ""

    number = 0
    for m in messages:
        result += process_message(m)
        number += 1

    if number == 0:
        return "You have no recent unread Office three six five emails."

    return "Here are your " + str(number) + " most recent unread Office three six five emails." + result
