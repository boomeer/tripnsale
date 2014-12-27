#!/bin/bash

git stash
git pull origin master
git stash pop
kill -SIGINT `cat /tmp/tripnsale.pid`
cd static
./lessr.js
cd ..
echo yes | ./manage.py collectstatic
./manage.py makemigrations --merge
./manage.py migrate
uwsgi --ini tripnsale/../tripnsale/uwsgi.ini
