# Python Standard Library Imports
import time
from datetime import datetime
from typing import Any


def get_media_upload_directory_path(instance: Any, filename: str) -> str:
    """A function that dynamially builds the uploaded fiels paths

    Args:
        instance (Any): Any Django Model's instance
        filename (str): File Name

    Returns:
        str: File Path
    """
    today = datetime.today().strftime("%d-%m-%Y")
    file_extension = filename.split(".")[-1]

    return "{0}s/{1}/{2}.{3}".format(
        instance.__class__.__name__.lower(),
        today,
        int(time.time()),
        file_extension.lower(),
    )
