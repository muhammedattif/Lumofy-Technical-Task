# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# Other Third Party Imports
from django_currentuser.middleware import get_current_authenticated_user


class AbstractModel(models.Model):
    """abstract model that is an entry point for common changes across all models"""

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active?"),
        help_text=_(
            "Designates whether this instance should be treated as active. "
            "Unselect this instead of deleting the instances.",
        ),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    created_by = models.ForeignKey(
        "src.User",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        default=get_current_authenticated_user,
        verbose_name=_("Created By"),
        related_name="%(class)s_created_by",
    )

    class Meta:
        abstract = True
