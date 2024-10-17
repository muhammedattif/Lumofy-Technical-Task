# Future Imports
from __future__ import annotations

# Python Standard Library Imports
from typing import TYPE_CHECKING

# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# First Party Imports
from src.utility.models import AbstractModel

from .lesson_progress import LessonProgress

if TYPE_CHECKING:
    from .course import Course
    from .student import Student


class Lesson(AbstractModel):
    """
    A model for Lesson
    """

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    # NOTE: Content may be video,audio, or text, so I choose text for now and we'll discuss if you need to support other types
    content = models.TextField(max_length=255, verbose_name=_("Content"))
    # NOTE: Assuming that the lesson will be added only to one course
    course = models.ForeignKey("src.Course", on_delete=models.CASCADE, related_name="lessons", verbose_name=_("Course"))

    class Meta(AbstractModel.Meta):
        db_table = "lessons"
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")

    def __str__(self):
        return f"{self.id}"

    # Factories

    @classmethod
    def create(cls, name: str, content: str, course: Course, description: str = None) -> Lesson:
        """Create a Lesson

        Args:
            name (str): Lesson's Name
            content (str): Lesson's Content
            course (Course): Course that this lesson will be related to
            description (str, optional): Lesson's Description. Defaults to None.

        Returns:
            Lesson: Created Lesson
        """

        return cls.objects.create(
            name=name,
            description=description,
            content=content,
            course=course,
        )

    # Queries

    def track(self, student: Student) -> bool:
        """Track a Lesson

        Args:
            student (Student): student that completed the lesson

        Returns:
            bool: True if Tracked, False otherwise
        """
        return bool(
            LessonProgress.get_or_create(
                student=student,
                lesson=self,
                is_completed=True,
            ),
        )

    def check_lesson_completion(self, student: Student) -> bool:
        """Check if this lesson is completed or not

        Returns:
            bool: True if completed, False otherwise
        """
        return LessonProgress.objects.filter(
            lesson=self,
            student=student,
        ).exists()
