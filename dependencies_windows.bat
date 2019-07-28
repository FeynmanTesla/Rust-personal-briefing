@ECHO OFF
cd src && py -m venv env && .\env\Scripts\activate && pip3 install -r assets/dependencies.txt && deactivate