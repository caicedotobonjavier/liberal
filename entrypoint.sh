#!/bin/bash
python manage.py migrate
exec gunicorn liberal.wsgi:application