# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.11.3-slim-bullseye

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED=1

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    git \
 && rm -rf /var/lib/apt/lists/*

# set the working directory
WORKDIR /app
# copy the repository files to it
COPY . /app
COPY requirements.* /app/

RUN pip install -U pip pip-tools wheel \
    && pip install -r requirements.txt

RUN python manage.py collectstatic --noinput --clear

# Port used by this container to serve HTTP.
EXPOSE 8000

# GUNICORN
CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "--threads", "2", "--worker-class", "gevent", "--max-requests-jitter", " 2000", "--max-requests", "1500", "wsgi"]
