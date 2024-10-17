"""
ASGI config for src project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# Python Standard Library Imports
import os

# Django Imports
from django.core.asgi import get_asgi_application

# Other Third Party Imports
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings." + config("ENVIRONMENT").lower())

application = get_asgi_application()
