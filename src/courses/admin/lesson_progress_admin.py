# Django Imports
from django.contrib import admin

# First Party Imports
from src.courses.models import LessonProgress


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_filter = [
        "lesson",
        "student",
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
        "lesson",
        "student",
        "created_by",
        "is_active",
        "created_at",
    ]
    list_select_related = ["lesson", "student", "created_by"]
    autocomplete_fields = ["lesson", "student"]
