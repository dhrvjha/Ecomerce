#!/bin/sh


# stop and exit with code 0
# if a command fails
set -e


# collects static files into STATIC_ROOT
# https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#collectstatic
python /admin/manage.py makemigrations
python /admin/manage.py migrate
python /admin/manage.py collectstatic --noinput



# uwsgi application
# --socket starts TCP socket
# :8000 on port 8000
# --master as master service "main" service
# --enable-threads enable multi-threading
uwsgi --socket :8000 --master --enable-threads --module admin.wsgi
