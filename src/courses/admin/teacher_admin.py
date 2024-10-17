# Django Imports
from django.contrib import admin

# First Party Imports
from src.courses.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_filter = [
        "user",
        "created_at",
        "updated_at",
        "created_by",
        "is_active",
    ]
    date_hierarchy = "created_at"
    readonly_fields = [
        "created_by",
        "created_at",
        "updated_at",
    ]
    list_display = [
        "id",
        "user",
        "created_by",
        "is_active",
        "created_at",
    ]
    list_select_related = ["user", "created_by"]
    search_fields = ["user__username"]
    autocomplete_fields = ["user"]
