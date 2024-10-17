# Other Third Party Imports
import factory
from factory import Faker

# First Party Imports
from src.courses.models import Lesson

from .course_factory import CourseFactory


class LessonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lesson

    name = Faker("sentence", nb_words=3)
    description = Faker("paragraph", nb_sentences=3)
    content = Faker("paragraph", nb_sentences=3)
    course = factory.SubFactory(CourseFactory)
