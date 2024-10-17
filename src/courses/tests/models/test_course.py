# Django Imports
from django.test import TestCase

# First Party Imports
from src.courses.factories import TeacherFactory
from src.courses.models import Course


class CourseModelTests(TestCase):
    """Course model tests"""

    def test_create_course_success(self):
        """test create: Success"""

        name = "Introduction to Testing"
        description = "A course about unit testing in Django."

        teacher = TeacherFactory.create()
        course = Course.create(
            name=name,
            description=description,
            teacher=teacher,
        )
        self.assertIsInstance(course, Course)
        self.assertEqual(course.name, name)
        self.assertEqual(course.description, description)
        self.assertEqual(course.teacher, teacher)
