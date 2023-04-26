#!/bin/bash

echo "BUILD START"

C:/Program\ Files/Python311/python.exe -m pip install -r requirements.txt
C:/Program\ Files/Python311/python.exe manage.py collectstatic --noinput --clear

echo "BUILD END"


