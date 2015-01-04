@echo off

cd static
node lessr.js
cd ..
py -3 manage.py collectstatic
py -3 manage.py migrate
py -3 manage.py runserver 0.0.0.0:8000

