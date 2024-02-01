"""Models for Utils App."""

import uuid
from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    """Model definition for BaseModel."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    available = models.BooleanField(_('Available'),default=True)
    created_at = models.DateField(_('Created at'), auto_now=False, auto_now_add=True)
    updated_at = models.DateField(_('Updated at'), auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
