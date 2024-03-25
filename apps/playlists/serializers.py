"""Serializers for Playlists App."""

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.contents.models import Anime
from apps.contents.serializers import AnimeMinimumSerializer
from apps.contents.serializers import MangaMinimumSerializer
from apps.playlists.models import Playlist
from apps.playlists.models import PlaylistAnime


class PlaylistSerializer(serializers.ModelSerializer):
    """Serializer for Playlist model."""

    class Meta:
        """Meta definition for PlaylistSerializer."""

        model = Playlist
        fields = [
            "id",
            "name",
            "created_at",
        ]


class PlaylistAnimeSerializer(serializers.ModelSerializer):
    """Serializer for PlaylistAnime model."""

    anime_id = serializers.UUIDField(write_only=True)
    anime = AnimeMinimumSerializer(read_only=True)

    class Meta:
        """Meta definition for PlaylistAnimeSerializer."""

        model = PlaylistAnime
        fields = [
            "id",
            "anime",
            "anime_id",
            "status",
            "is_watched",
            "is_favorite",
        ]  # Add order field

        def create(self, validated_data):
            anime_id = validated_data.pop("anime_id")
            anime = get_object_or_404(Anime, id=anime_id)
            playlist_anime = PlaylistAnime.objects.create(
                anime=anime,
                **validated_data,
            )
            return playlist_anime


class PlaylistMangaSerializer(serializers.ModelSerializer):
    """Serializer for PlaylistManga model."""

    manga = MangaMinimumSerializer(read_only=True)

    class Meta:
        """Meta definition for PlaylistMangaSerializer."""

        model = PlaylistAnime
        fields = [
            "id",
            "manga",
            "status",
            "is_watched",
            "is_favorite",
        ]  # Add order field
