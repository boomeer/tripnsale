#!/bin/bash

git stash
git pull origin master
git stash pop
kill -SIGINT `cat /tmp/tripnsale_dev.pid`
cd static
./lessr.js
cd ..
./manage.py collectstatic
./manage.py makemigrations
./manage.py migrate
uwsgi --ini tripnsale/uwsgi.ini
