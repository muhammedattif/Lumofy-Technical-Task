# Future Imports
from __future__ import annotations

# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# First Party Imports
from src.utility.models import AbstractModel

from . import Course, Enrollment


class Student(AbstractModel):
    """
    A model for Student
    """

    user = models.OneToOneField("src.User", on_delete=models.CASCADE, related_name="student", verbose_name=_("User"))
    # Add fields related to the students

    class Meta(AbstractModel.Meta):
        db_table = "students"
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self):
        return f"{self.id}"

    def get_enrolled_courses(self) -> models.QuerySet[Course]:
        """Retrive Enrolled courses for student

        Returns:
            models.QuerySet[Course]: Enrolled courses queryset
        """
        courses_ids = Enrollment.objects.filter(student=self).values_list("course", flat=True)
        return Course.objects.filter(id__in=courses_ids)
