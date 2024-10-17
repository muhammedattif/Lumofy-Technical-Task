# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA

# First Party Imports
from src.users.models import User


@admin.register(User)
class UserAdmin(UA):
    list_filter = [
        "created_at",
        "updated_at",
        "is_staff",
        "is_staff",
        "is_active",
    ]
    ordering = ["-created_at"]
    date_hierarchy = "created_at"
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    list_display = (
        "id",
        "email",
        "username",
        "is_staff",
        "is_active",
        "created_at",
    )
    search_fields = (
        "email",
        "username",
    )
    fieldsets = (
        (
            "User Information",
            {
                "fields": (
                    "email",
                    "username",
                    "created_at",
                    "updated_at",
                ),
            },
        ),
        (
            "Permissions",
            {
                "classes": ["collapse"],
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Password", {"classes": ["collapse"], "fields": ("password",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
