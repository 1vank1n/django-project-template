from django.db import models
from django.utils.timezone import now

from .models import Common


class ActualManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            publication_date__lte=now(),
            status=Common.STATUS.published,
        )
        return queryset
