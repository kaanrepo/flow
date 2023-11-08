#!/bin/bash

SUPERUSER_NAME=${SUPERUSER_NAME:-admin}

cd /app

/opt/venv/bin/python3 manage.py migrate --noinput
/opt/venv/bin/python3 manage.py createsuperuser --noinput --username ${SUPERUSER_NAME} || true