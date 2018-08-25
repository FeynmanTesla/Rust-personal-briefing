import outlook
office365EmailAddress = open("office365EmailAddress.txt","r").read()
office365EmailPassword = open("office365EmailPassword.txt","r").read()

mail = outlook.Outlook()
mail.login('emailaccount@live.com','yourpassword')
mail.inbox()
print mail.unread()