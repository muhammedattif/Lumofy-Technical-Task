# Django Imports
from django.db.models.signals import post_save
from django.dispatch import receiver

# REST Framework Imports
from rest_framework.authtoken.models import Token

# First Party Imports
from src.users.models import User


@receiver(post_save, sender=User)
def user_post_save_signal(instance, created, *args, **kwargs):
    """
    User post_save
        1- Create Token
    """
    if created:
        # Create Token
        Token.objects.create(user=instance)
