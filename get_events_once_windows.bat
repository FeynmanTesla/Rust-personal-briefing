@ECHO OFF
cd src && py -m venv env && .\env\Scripts\activate && python -c "from get_events import get_events; print(get_events())" && deactivate && cd ..
deactivate
cd ..