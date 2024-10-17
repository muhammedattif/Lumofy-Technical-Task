# Django Imports
from django.test import TestCase

# First Party Imports
from src.courses.factories import CourseFactory, EnrollmentFactory, LessonFactory, LessonProgressFactory, StudentFactory
from src.courses.models import Lesson


class LessonModelTests(TestCase):
    """Lesson model tests"""

    def test_create_success(self):
        """test create: success"""

        name = "Introduction to Testing"
        description = "A course about unit testing in Django."
        content = "A course about unit testing in Django."

        course = CourseFactory.create()
        lesson = Lesson.create(
            course=course,
            name=name,
            description=description,
            content=content,
        )
        self.assertIsInstance(lesson, Lesson)
        self.assertEqual(lesson.name, name)
        self.assertEqual(lesson.description, description)
        self.assertEqual(lesson.content, content)

    #####

    def test_track(self):
        """test track: Success"""

        lesson = LessonFactory.create()
        student = StudentFactory.create()
        EnrollmentFactory.create(course=lesson.course, student=student)

        self.assertTrue(lesson.track(student=student))

    ####

    def test_check_lesson_completion_success(self):
        "test check_lesson_completion: success"

        lesson = LessonFactory.create()
        student = StudentFactory.create()
        EnrollmentFactory.create(course=lesson.course, student=student)
        LessonProgressFactory.create(student=student, lesson=lesson)

        self.assertTrue(lesson.check_lesson_completion(student=student))
