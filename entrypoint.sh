#!/bin/sh

echo 'Apply migrations...'
python manage.py migrate

echo 'Collect static files...'
python manage.py collectstatic --no-input

echo 'Start uwsgi...'
uwsgi \
    --strict \
    --master \
    --enable-threads \
    --vacuum \
    --need-app \
    --thunder-lock \
    --disable-logging \
    --log-4xx \
    --log-5xx \
    --max-requests 500 \
    --max-worker-lifetime 3600 \
    --chdir /app/ \
    --socket 0.0.0.0:9000 \
    --wsgi-file src/wsgi.py \
    --processes 4 \
    --threads 4 \
    --protocol uwsgi \
    --buffer-size 65535 \
    --env DJANGO_SETTINGS_MODULE=src.settings.production

exec "$@"
