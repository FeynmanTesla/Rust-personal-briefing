#!/bin/bash
cd src && python3 -m venv env && source env/bin/activate && pip3 install -r assets/dependencies.txt && deactivate