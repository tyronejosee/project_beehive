"""Viewsets for Studios App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.utils.translation import gettext as _
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.utils.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.utils.pagination import LargeSetPagination
from apps.users.permissions import IsContributor
from apps.animes.models import Anime
from apps.animes.serializers import AnimeMinimalSerializer
from .models import Studio
from .serializers import StudioReadSerializer, StudioWriteSerializer
from .schemas import studio_schemas


@extend_schema_view(**studio_schemas)
class StudioViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Studio instances.

    Endpoints:
    - GET /api/v1/studios/
    - POST /api/v1/studios/
    - GET /api/v1/studios/{id}/
    - PUT /api/v1/studios/{id}/
    - PATCH /api/v1/studios/{id}/
    - DELETE /api/v1/studios/{id}/
    """

    permission_classes = [IsContributor]
    serializer_class = StudioWriteSerializer
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        return Studio.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return StudioReadSerializer
        return super().get_serializer_class()

    @extend_schema(
        summary="Get Animes for Studio",
        description="Retrieve a list of animes for studio.",
    )
    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="animes",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_animes(self, request, *args, **kwargs):
        """
        Action retrieve animes associated with a studio.

        Endpoints:
        - GET /api/v1/studios/{id}/animes/
        """
        studio = self.get_object()

        try:
            animes = Anime.objects.get_by_studio(studio)
            if animes.exists():
                paginator = LargeSetPagination()
                result_page = paginator.paginate_queryset(animes, request)
                serializer = AnimeMinimalSerializer(result_page, many=True)
                return paginator.get_paginated_response(serializer.data)
            return Response(
                {"detail": _("No animes found for this studio.")},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
