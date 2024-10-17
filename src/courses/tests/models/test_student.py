# Django Imports
from django.test import TestCase

# First Party Imports
from src.courses.factories import CourseFactory, EnrollmentFactory, StudentFactory
from src.courses.models import Course


class StudentModelTests(TestCase):
    """Student model tests"""

    def test_get_enrolled_courses_success(self):
        """test get_enrolled_courses: Success"""

        course_1 = CourseFactory.create()
        course_2 = CourseFactory.create()
        student = StudentFactory.create()
        EnrollmentFactory.create(course=course_1, student=student)
        EnrollmentFactory.create(course=course_2, student=student)

        expected_enrolled_courses_queryset = Course.objects.filter(id__in={course_1.id, course_2.id})
        self.assertQuerySetEqual(student.get_enrolled_courses(), expected_enrolled_courses_queryset, ordered=False)
