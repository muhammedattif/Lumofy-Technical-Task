# REST Framework Imports
from rest_framework.permissions import BasePermission


class TeacherPermission(BasePermission):
    """TeacherPermission class"""

    def has_permission(self, request, view):
        if request.user.is_teacher:
            return True
        return False
