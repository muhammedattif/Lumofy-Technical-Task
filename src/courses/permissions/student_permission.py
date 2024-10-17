# REST Framework Imports
from rest_framework.permissions import BasePermission


class StudentPermission(BasePermission):
    """StudentPermission class"""

    def has_permission(self, request, view):
        if request.user.is_student:
            return True
        return False
