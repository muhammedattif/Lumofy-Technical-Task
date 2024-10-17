# Django Imports
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class FileSizeValidator:
    message = _(
        "Max file size is “%(max_size)s”. " "Current file size is : %(current_size)s.",
    )
    code = "invalid_size"

    def __init__(self, max_size: int, message: str = None, code: str = None):
        self.max_size = max_size
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):

        filesize = value.size
        if filesize > self.max_size:
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    "max_size": filesizeformat(self.max_size),
                    "current_size": filesizeformat(filesize),
                    "value": value,
                },
            )

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.message == other.message and self.code == other.code
