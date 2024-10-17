# Django Imports
from django.contrib import admin

# First Party Imports
from src.courses.models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_filter = [
        "course",
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
        "course",
        "created_by",
        "is_active",
        "created_at",
    ]
    list_select_related = ["course", "created_by"]
    search_fields = [
        "name",
        "description",
    ]
    autocomplete_fields = ["course"]
