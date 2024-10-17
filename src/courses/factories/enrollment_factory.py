# Other Third Party Imports
import factory
from factory import Faker

# First Party Imports
from src.courses.models import Enrollment

from .course_factory import CourseFactory
from .student_factory import StudentFactory


class EnrollmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Enrollment

    course = factory.SubFactory(CourseFactory)
    student = factory.SubFactory(StudentFactory)
    enrolled_at = Faker("date_between", start_date="today", end_date="+30d")
