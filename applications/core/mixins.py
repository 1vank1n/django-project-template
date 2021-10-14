from django.utils.safestring import mark_safe


class ImageAdminMixin:
    """
    Позволяет отображать изображение в административной панели
    """
    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50")

    get_image.short_description = 'Изображение'


class StaffQuerysetMixin:
    def get_queryset(self):
        if self.request.user.is_staff:
            self.queryset = self.model.objects.all()
        return super().get_queryset()
