#!/bin/bash

kill -SIGINT `cat /tmp/tripnsale.pid`
cd static
./lessr.js
cd ..
./manage.py collectstatic
./manage.py makemigrations
./manage.py migrate
uwsgi --ini tripnsale/uwsgi.ini
