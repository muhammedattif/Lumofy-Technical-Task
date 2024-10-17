"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# Python Standard Library Imports
import os

# Django Imports
from django.core.wsgi import get_wsgi_application

# Other Third Party Imports
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings." + config("ENVIRONMENT").lower())


application = get_wsgi_application()
