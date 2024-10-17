# Django Imports
from django.contrib import admin

# First Party Imports
from src.courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = [
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
        "name",
        "teacher",
        "created_by",
        "is_active",
        "created_at",
    ]
    list_select_related = ["teacher", "created_by"]
    search_fields = [
        "created_by__username",
    ]
    autocomplete_fields = ["teacher"]
    search_fields = ["name"]
