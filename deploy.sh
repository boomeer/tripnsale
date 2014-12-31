#!/bin/bash

git stash
if [ $# -eq 0 ] ; then
    git pull origin master
else
    git pull origin $1
fi
git stash pop
kill -SIGINT `cat /tmp/tripnsale.pid`
cd static
./lessr.js
cd ..
echo yes | ./manage.py collectstatic
./manage.py migrate
uwsgi --ini tripnsale/../tripnsale/uwsgi.ini
