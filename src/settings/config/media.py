# Python Standard Library Imports
import os

from .main import BASE_DIR

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

# File Uploads
DATA_UPLOAD_MAX_MEMORY_SIZE = 200000000  # 200 MB
