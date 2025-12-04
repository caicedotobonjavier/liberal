#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py migrate --settings=liberal.settings.prod
python manage.py collectstatic --noinput --settings=liberal.settings.prod