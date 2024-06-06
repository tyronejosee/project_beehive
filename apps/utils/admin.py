"""Admin for Utils App."""

from django.contrib import admin

from .models import Picture, Video


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    """Admin for Picture model."""

    list_per_page = 25
    search_fields = [
        "name",
        "object_id",
    ]
    list_display = [
        "name",
        "image",
        "content_type",
    ]
    list_filter = [
        "is_available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """Admin for Video model."""

    list_per_page = 25
    search_fields = [
        "object_id",
    ]
    list_display = [
        "object_id",
        "content_type",
    ]
    list_filter = [
        "is_available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
