# Django Imports
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# First Party Imports
from src.utility.models import AbstractModel


class User(AbstractModel, AbstractUser):
    """User Model"""

    class Meta:
        db_table = "users"
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    # Properties

    @property
    def is_teacher(self) -> bool:
        """Check if this user has a teacher profile or not

        Returns:
            bool: True if has teacher profle, False Otherwise
        """
        return hasattr(self, "teacher")

    @property
    def is_student(self) -> bool:
        """Check if this user has a student profile or not

        Returns:
            bool: True if has student profle, False Otherwise
        """
        return hasattr(self, "student")
