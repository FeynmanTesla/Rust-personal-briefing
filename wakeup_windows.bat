@ECHO OFF
cd src && .\env\Scripts\activate && python wakeup.py && deactivate && cd ..
deactivate
cd ..