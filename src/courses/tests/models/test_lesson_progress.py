# Django Imports
from django.test import TestCase

# First Party Imports
from src.courses.factories import LessonFactory, LessonProgressFactory, StudentFactory
from src.courses.models import LessonProgress


class LessonProgressModelTests(TestCase):
    """LessonProgress model tests"""

    def test_get_or_create_created(self):
        """test get_or_create: Created"""

        student = StudentFactory.create()
        lesson = LessonFactory.create()
        lesson_progress = LessonProgress.get_or_create(
            student=student,
            lesson=lesson,
            is_completed=True,
        )
        self.assertIsInstance(lesson_progress, LessonProgress)
        self.assertEqual(lesson_progress.lesson, lesson)
        self.assertEqual(lesson_progress.student, student)
        self.assertTrue(lesson_progress.is_completed)

    def test_get_or_create_created_before(self):
        """test get_or_create: Created"""

        student = StudentFactory.create()
        lesson = LessonFactory.create()

        LessonProgressFactory.create(student=student, lesson=lesson)

        lesson_progress = LessonProgress.get_or_create(
            student=student,
            lesson=lesson,
            is_completed=True,
        )
        self.assertIsInstance(lesson_progress, LessonProgress)
        self.assertEqual(lesson_progress.lesson, lesson)
        self.assertEqual(lesson_progress.student, student)
        self.assertTrue(lesson_progress.is_completed)
        self.assertEqual(LessonProgress.objects.filter(student=student, lesson=lesson).count(), 1)
