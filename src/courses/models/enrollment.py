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
    # Python Standard Library Imports
    from datetime import datetime

    from .course import Course
    from .student import Student


class Enrollment(AbstractModel):
    """
    A model for Enrollment
    """

    course = models.ForeignKey("src.Course", on_delete=models.CASCADE, verbose_name=_("Course"))
    student = models.ForeignKey("src.Student", on_delete=models.CASCADE, verbose_name=_("Student"))
    enrolled_at = models.DateTimeField(verbose_name=_("Enrolled At"))

    class Meta(AbstractModel.Meta):
        db_table = "enrollments"
        verbose_name = _("Enrollment")
        verbose_name_plural = _("Enrollments")
        constraints = [
            models.UniqueConstraint(fields=["course", "student"], name="Unique_course_and_student"),
        ]

    def __str__(self):
        return f"{self.id}"

    # Factories

    @classmethod
    def create(cls, course: Course, student: Student, enrolled_at: datetime) -> Enrollment:
        """Create an enrollment for a student in a course

        Args:
            course (Course): Course that the user will enrolled to
            student (Student): Student that will be enrolled
            enrolled_at (datetime): Enrollment datetime

        Returns:
            Enrollment: Created Enrollment
        """

        return cls.objects.create(
            course=course,
            student=student,
            enrolled_at=enrolled_at,
        )
