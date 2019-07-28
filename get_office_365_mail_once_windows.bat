@ECHO OFF
cd src && py -m venv env && .\env\Scripts\activate && python -c "from get_office_365_emails import get_office_365_emails; print(get_office_365_emails())" && deactivate && cd ..
deactivate
cd ..