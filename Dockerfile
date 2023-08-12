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

# UWSGI
# See recommendations here: 
# https://www.bloomberg.com/company/stories/configuring-uwsgi-production-deployment/
CMD uwsgi --http=0.0.0.0:8000 --master --module=wsgi \
    --strict \
    # number of worker processes
    --processes=5 \
    --enable-threads \
    # Delete sockets during shutdown
    --vacuum \
    --single-interpreter \
    # Shutdown when receiving SIGTERM (default is respawn)
    --die-on-term \
    --need-app \
    # if root, uwsgi can drop privileges from djangoproject.com
    --uid=1000 --gid=2000 \
    # respawn processes taking more than 20 seconds
    --harakiri=20 \
    # Restart workers after this many requests
    --max-requests=5000 \
    # set cheaper algorithm to use, if not set default will be used
    # see https://uwsgi-docs.readthedocs.io/en/latest/Cheaper.html
    --cheaper-algo=spare \
    # minimum number of workers to keep at all times
    --cheaper=2 \
    # number of workers to spawn at startup
    --cheaper-initial=3 \
    # maximum number of workers that can be spawned
    --workers=5 \
    # how many workers should be spawned at a time
    --cheaper-step=1 \
    # soft limit will prevent cheaper from spawning new workers
    # if workers total rss memory is equal or higher
    # we use 128MB soft limit below (values are in bytes)
    --cheaper-rss-limit-soft=134217728 \
    # Restart workers after this much resident memory
    --reload-on-rss=2048 \
    # How long to wait before forcefully killing workers
    --worker-reload-mercy=20 \
    --ignore-write-errors \
    --disable-write-exception \
    # Disable built-in logging 
    --disable-logging \
    # but log 4xx's anyway
    --log-4xx \
    # and 5xx's
    --log-5xx