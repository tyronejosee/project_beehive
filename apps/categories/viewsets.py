"""Viewsets for Contents App."""

from django.utils.translation import gettext as _
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.mixins import LogicalDeleteMixin
from apps.utils.permissions import IsStaffOrReadOnly
from apps.contents.models import Anime
from apps.contents.serializers import AnimeSerializer
from apps.categories.models import Url, Studio, Genre, Season, Demographic
from apps.categories.serializers import (
    UrlSerializer, StudioSerializer, GenreSerializer, SeasonSerializer, DemographicSerializer
)


class UrlViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Url instances.
    """
    serializer_class = UrlSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['url', 'tag']
    ordering_fields = ['tag']
    ordering = ['id']

    def get_queryset(self):
        return Url.objects.filter(available=True)


class StudioViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Studio instances.
    """
    serializer_class = StudioSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Studio.objects.filter(available=True)

    @action(detail=True, methods=['get'], url_path='animes')
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified studio.
        """
        studio = self.get_object()
        anime_list = Anime.objects.filter(studio_id=studio)
        if anime_list.exists():
            serializer = AnimeSerializer(anime_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'detail': _('There are no animes for this studio.')}, status=status.HTTP_404_NOT_FOUND
        )


class GenreViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Genre instances.
    """
    serializer_class = GenreSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['name',]
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Genre.objects.filter(available=True)

    @action(detail=True, methods=['get'], url_path='animes')
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified genre.
        """
        genre = self.get_object()
        anime_list = Anime.objects.filter(genre_id=genre)
        if anime_list.exists():
            serializer = AnimeSerializer(anime_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'detail': _('There are no animes for this genre.')}, status=status.HTTP_404_NOT_FOUND
        )


class SeasonViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Season instances.
    """
    serializer_class = SeasonSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Season.objects.filter(available=True)


class DemographicViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Demographic instances.
    """
    serializer_class = DemographicSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Demographic.objects.filter(available=True)