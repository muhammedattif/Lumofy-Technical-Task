# Other Third Party Imports
import factory

# First Party Imports
from src.courses.models import Student
from src.users.factories import UserFactory


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    user = factory.SubFactory(UserFactory)
