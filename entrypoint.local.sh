#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo 'Apply migrations...'
python manage.py migrate

echo 'Runserver...'
python manage.py runserver 0.0.0.0:9000

echo 'Collect static files...'
python manage.py collectstatic --no-input

exec "$@"
