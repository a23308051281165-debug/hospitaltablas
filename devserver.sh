#!/bin/sh
source .venv/bin/activate
python backend_Hospital/manage.py runserver $PORT
