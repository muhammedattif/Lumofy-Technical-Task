# Python Standard Library Imports
from datetime import datetime

# Django Imports
from django.test import TestCase

# First Party Imports
from src.courses.factories import CourseFactory, StudentFactory
from src.courses.models import Enrollment


class CourseModelTests(TestCase):
    """Course model tests"""

    def test_create_course_success(self):
        """test create: Success"""

        now = datetime.now()
        student = StudentFactory.create()
        course = CourseFactory.create()
        enrollment = Enrollment.create(
            student=student,
            course=course,
            enrolled_at=now,
        )
        self.assertIsInstance(enrollment, Enrollment)
        self.assertEqual(enrollment.course, course)
        self.assertEqual(enrollment.student, student)
        self.assertEqual(enrollment.enrolled_at, now)
