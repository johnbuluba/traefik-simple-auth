#!/bin/sh

cd $(dirname "$0")/../traefikauth

echo Migrating
./manage.py migrate


# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn traefikauth.wsgi:application \
    --capture-output \
    --enable-stdio-inheritance \
    --bind 0.0.0.0:8000 \
    --workers 3