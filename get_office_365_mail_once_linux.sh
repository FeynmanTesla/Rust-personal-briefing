#!/bin/bash
cd src && source env/bin/activate && .\env\Scripts\activate && python3 -c "from get_office_365_emails import get_office_365_emails; print(get_office_365_emails())" && deactivate && cd ..