# Django Imports
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SrcConfig(AppConfig):
    """Django Apps Config class"""

    name = "src"
    verbose_name = "src"

    def ready(self):
        from . import signals  # noqa
