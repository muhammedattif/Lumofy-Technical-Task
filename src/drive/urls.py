# REST Framework Imports
from rest_framework.routers import SimpleRouter

from .views import v1

uploaded_files_router_v1 = SimpleRouter(trailing_slash=True)
uploaded_files_router_v1.register(r"files", v1.UploadedFilesViewSet, basename="")
