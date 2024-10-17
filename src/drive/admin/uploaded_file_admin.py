# Django Imports
from django.contrib import admin

# First Party Imports
from src.drive.models import UploadedFile


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
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
    list_display = (
        "id",
        "size",
        "type",
        "created_by",
        "is_active",
        "created_at",
    )
    list_select_related = ["created_by"]
    search_fields = ("created_by__username",)
