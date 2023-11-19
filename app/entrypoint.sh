#!/bin/bash

APP_PORT=${PORT:-8000}

cd /app/

# /opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm flow.wsgi:application --bind "0.0.0.0:${APP_PORT}"

/opt/venv/bin/daphne -b 0.0.0.0 -p 8000 flow.asgi:application 
