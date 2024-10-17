# REST Framework Imports
from rest_framework.routers import SimpleRouter

from .views import v1

auth_router_v1 = SimpleRouter(trailing_slash=False)
auth_router_v1.register(r"", v1.AuthViewSet, basename="")
auth_router_v1.register(r"reset-password", v1.ResetPasswordViewSet, basename="reset-password")
auth_router_v1.register(r"signup", v1.SignUpViewSet, basename="signup")
auth_router_v1.register(r"roles", v1.RolesViewSet, basename="roles")
auth_router_v1.register(r"permissions", v1.PermissionsViewSet, basename="permissions")
auth_router_v1.register(r"users", v1.UsersViewSet, basename="users")
