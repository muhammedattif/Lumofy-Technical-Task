# REST Framework Imports
from rest_framework.routers import SimpleRouter

from .views import v1

courses_router_v1 = SimpleRouter(trailing_slash=True)
courses_router_v1.register(r"", v1.CoursesViewSet, basename="")
