"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# Python Standard Library Imports
from pathlib import Path

# Other Third Party Imports
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
ENVIRONMENT = config("ENVIRONMENT", default="LOCAL")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="")

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")], default="localhost")
CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",
    cast=lambda v: [s.strip() for s in v.split(",")],
    default="localhost",
)

ROOT_URLCONF = "src.urls"

WSGI_APPLICATION = "src.wsgi.application"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "src.User"

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

# Django Admin
SITE_INDEX_TITLE = "LMS Administration"
SITE_TITLE = "Administration"
SITE_HEADER = "LMS Administration"
