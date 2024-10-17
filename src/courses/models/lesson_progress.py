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
    from .lesson import Lesson
    from .student import Student

# Django Imports
from django.core.exceptions import ValidationError


class LessonProgress(AbstractModel):
    """
    A model for LessonProgress
    """

    lesson = models.ForeignKey("src.Lesson", on_delete=models.CASCADE, verbose_name=_("Lesson"))
    student = models.ForeignKey("src.Student", on_delete=models.CASCADE, verbose_name=_("Student"))
    is_completed = models.BooleanField(default=False, verbose_name=_("Is Completed"))

    class Meta(AbstractModel.Meta):
        db_table = "lessons_progress"
        verbose_name = _("Lesson Progress")
        verbose_name_plural = _("Lessons Progress")
        constraints = [
            models.UniqueConstraint(fields=["lesson", "student"], name="Unique_lesson_and_student"),
        ]

    def clean(self):

        if not self.student.get_enrolled_courses().filter(id=self.lesson.course_id).exists():
            raise ValidationError({"lesson": "Student must enroll the course to track its lessons"})

    def __str__(self):
        return f"{self.id}"

    # Factories

    @classmethod
    def get_or_create(cls, lesson: Lesson, student: Student, is_completed: bool = False) -> LessonProgress:
        """Get or Create Lesson Progress

        Args:
            lesson (Lesson): Lesson the will be tracked
            student (Student): Student who completed the lesson
            is_completed (bool): Indicated whether the lesson completed or not

        Returns:
            LessonProgress: Created LessonProgress
        """

        lesson_progress, created = cls.objects.get_or_create(
            lesson=lesson,
            student=student,
            defaults={
                "is_completed": is_completed,
            },
        )
        if not created and not lesson_progress.is_completed:
            lesson_progress.is_completed = True
            lesson_progress.save()

        return lesson_progress
