#!/bin/bash

# Based on: https://simpleisbetterthancomplex.com/tutorial/2016/10/14/how-to-deploy-to-digital-ocean.html

NAME="rekik_eng"
DIR=/home/rekik/rekikeng
USER=rekik
GROUP=rekik
WORKERS=3
BIND=unix:/home/rekik/run/gunicorn.sock
DJANGO_SETTINGS_MODULE=core.settings
DJANGO_WSGI_MODULE=core.wsgi
LOG_LEVEL=error

cd $DIR
source ../bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DIR:$PYTHONPATH

exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $WORKERS \
  --user=$USER \
  --group=$GROUP \
  --bind=$BIND \
  --log-level=$LOG_LEVEL \
  --log-file=-