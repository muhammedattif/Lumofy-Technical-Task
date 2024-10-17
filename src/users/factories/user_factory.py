# Other Third Party Imports
import factory
from factory import Faker

# First Party Imports
from src.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("user_name")
    email = Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "defaultpassword")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
