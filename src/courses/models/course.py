# Future Imports
from __future__ import annotations

# Python Standard Library Imports
from typing import TYPE_CHECKING

# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# First Party Imports
from src.utility.models import AbstractModel

if TYPE_CHECKING:
    from .teacher import Teacher


class Course(AbstractModel):
    """
    A model for Course
    """

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    teacher = models.ForeignKey("src.Teacher", on_delete=models.CASCADE, related_name="courses")

    class Meta(AbstractModel.Meta):
        db_table = "courses"
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return f"{self.id}"

    # Factories

    @classmethod
    def create(cls, name: str, description: str, teacher: Teacher) -> Course:
        """Create a course

        Args:
            name (str): Course's Name
            description (str): Course's Description

        Returns:
            Course: Created Course
        """

        return cls.objects.create(
            name=name,
            description=description,
            teacher=teacher,
        )
