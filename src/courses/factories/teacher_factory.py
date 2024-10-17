# Other Third Party Imports
import factory

# First Party Imports
from src.courses.models import Teacher
from src.users.factories import UserFactory


class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Teacher

    user = factory.SubFactory(UserFactory)
