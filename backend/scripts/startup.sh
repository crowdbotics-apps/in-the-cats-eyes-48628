#!/bin/bash

python manage.py migrate --noinput

waitress-serve --port=$PORT in_the_cats_eyes_48628.wsgi:application
