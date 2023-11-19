FROM python:3.9.7-slim-buster

# Set the working directory to /app
COPY . /app
WORKDIR /app
RUN python3 -m venv /opt/venv

ENV DJANGO_SETTINGS_MODULE=flow.settings_dev.base

# Install any needed packages specified in requirements.txt
RUN /opt/venv/bin/pip install --upgrade pip && /opt/venv/bin/pip install -r requirements.txt && chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]