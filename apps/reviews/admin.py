"""Admin for Reviews App."""

from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin for Review model."""

    ordering = ["user"]
    list_per_page = 25
    search_fields = [
        "user",
    ]
    list_display = [
        "user",
        "comment",
        "is_available",
    ]
    list_filter = [
        "rating",
        "is_spoiler",
    ]
    list_editable = [
        "is_available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
