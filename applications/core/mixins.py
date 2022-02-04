from django.utils.timezone import now

from .models import Common


class CommonQuerysetMixin:
    """Доступ к просмотру черновиков (Common.STATUS.draft)"""

    def get_queryset(self):
        self.queryset = super().get_queryset()

        user = self.request.user
        if user.is_authenticated and user.is_active and user.is_team:
            return self.queryset

        self.queryset = self.queryset.filter(status=Common.STATUS.published)
        return self.queryset


class PublishedQuerysetMixin(CommonQuerysetMixin):
    """Доступ к просмотр опубликованных сущностей"""

    def get_queryset(self):
        super().get_queryset()

        user = self.request.user
        if not user.is_authenticated or not user.is_team:
            self.queryset = self.queryset.filter(published_at__lte=now())
        return self.queryset
