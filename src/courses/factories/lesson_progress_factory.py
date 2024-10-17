# Other Third Party Imports
import factory

# First Party Imports
from src.courses.models import LessonProgress

from .lesson_factory import LessonFactory
from .student_factory import StudentFactory


class LessonProgressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LessonProgress

    lesson = factory.SubFactory(LessonFactory)
    student = factory.SubFactory(StudentFactory)
    is_completed = False
