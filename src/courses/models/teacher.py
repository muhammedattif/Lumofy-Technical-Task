# Future Imports
from __future__ import annotations

# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# First Party Imports
from src.utility.models import AbstractModel


class Teacher(AbstractModel):
    """
    A model for Teacher
    """

    user = models.OneToOneField("src.User", on_delete=models.CASCADE, related_name="teacher", verbose_name=_("User"))
    # Add fields related to the teachers

    class Meta(AbstractModel.Meta):
        db_table = "teachers"
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

    def __str__(self):
        return f"{self.id}"
