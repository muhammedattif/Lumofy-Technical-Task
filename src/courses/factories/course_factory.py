# Other Third Party Imports
import factory
from factory import Faker

# First Party Imports
from src.courses.models import Course

from .teacher_factory import TeacherFactory


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    name = Faker("sentence", nb_words=3)
    description = Faker("paragraph", nb_sentences=3)
    teacher = factory.SubFactory(TeacherFactory)
