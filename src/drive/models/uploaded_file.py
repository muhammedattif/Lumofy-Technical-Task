# Future Imports
from __future__ import annotations

# Django Imports
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import FileExtensionValidator, get_available_image_extensions
from django.db import models
from django.utils.translation import gettext_lazy as _

# Other Third Party Imports
from django_currentuser.middleware import get_current_authenticated_user

# First Party Imports
from src.utility.functions import get_media_upload_directory_path
from src.utility.models import AbstractModel
from src.utility.validators import FileSizeValidator


class UploadedFile(AbstractModel):
    """
    A model for uploading files
    """

    # Constants
    MAX_FILE_SIZE = 1024  # 1 MB
    SIZE_UNIT = "bytes"

    file = models.FileField(
        upload_to=get_media_upload_directory_path,
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf", *get_available_image_extensions()]),
            FileSizeValidator(max_size=MAX_FILE_SIZE),
        ],  # Fox Example we will only allow MP4 and Excel Files
        verbose_name=_("File"),
    )
    type = models.CharField(max_length=50, verbose_name=_("Type"))  # pylint: disable=redefined-builtin
    size = models.PositiveIntegerField(verbose_name=_("Size"))
    created_by = models.ForeignKey(
        "src.User",
        on_delete=models.CASCADE,
        default=get_current_authenticated_user,
        verbose_name=_("Created By"),
        related_name="files",
    )

    class Meta(AbstractModel.Meta):
        db_table = "uploaded_files"
        verbose_name = _("Uploaded File")
        verbose_name_plural = _("Uploaded Files")

    # Factories

    @classmethod
    def create(cls, file: InMemoryUploadedFile) -> UploadedFile:
        """Create an Uploaded File

        Args:
            file (InMemoryUploadedFile): File that will be uploaded

        Returns:
            UploadedFile: Created UploadedFile Instance
        """

        return cls.objects.create(
            file=file,
            size=file.size,
            type=file.name.split(".")[-1],
        )
