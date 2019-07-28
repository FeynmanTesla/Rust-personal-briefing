#!/bin/bash
cd src && source env/bin/activate && .\env\Scripts\activate && python3 -c "from get_events import get_events; print(get_events())" && deactivate && cd ..