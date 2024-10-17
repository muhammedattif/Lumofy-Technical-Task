ARG PLATFORM
FROM --platform=${PLATFORM:-linux/amd64} python:3.8.15-slim-bullseye as base

# set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin gettext libzbar-dev gcc libgnutls28-dev libgdal-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install psycopg2 only if the platform is linux/arm64 must be after installing the requirements.txt
RUN if [ "$PLATFORM" = "linux/arm64" ] ; then pip install psycopg2==2.9.3; fi

# copy project
COPY . .
RUN mkdir -p media
RUN mkdir -p static
RUN mkdir -p logs

# Django Local
FROM base as app-local
COPY ./entrypoint.local.sh /usr/local/bin/entrypoint.local.sh
RUN chmod +x /usr/local/bin/entrypoint.local.sh
CMD ["entrypoint.local.sh"]


# Django Prod and Staging
FROM base as app
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
CMD ["entrypoint.sh"]
