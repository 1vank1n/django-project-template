from django.contrib import admin
from django.utils.html import mark_safe

from . import models


class CommonAdmin(admin.ModelAdmin):
    list_filter = ['status', 'created']
    readonly_fields = ['created', 'modified']
    actions = ['make_published', 'make_drafted']

    def make_published(self, request, queryset):
        queryset.update(status=models.Common.STATUS.published)
    make_published.short_description = 'Выставить статус "Опубликовано"' # yapf: disable

    def make_drafted(self, request, queryset):
        queryset.update(status=models.Common.STATUS.draft)
    make_drafted.short_description = 'Выставить статус "Черновик"' # yapf: disable


class CommonInlineAdmin:
    readonly_fields = ['created', 'modified']


class SeoFieldsAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        newfieldsets = list(fieldsets)
        fields = ['seo_title', 'seo_keywords', 'seo_description']
        for f in fields:
            newfieldsets[0][1]['fields'].remove(f)
        newfieldsets.append(['SEO', {'classes': ('collapse', ), 'fields': fields}])
        return newfieldsets


class ThumbAdminMixin():
    image_list = []

    def __init__(self, *args, **kwargs):
        if self.image_list:
            for image in self.image_list:
                name = 'thumb_{}'.format(image)

                def fn(obj):
                    photo = getattr(obj, image)  # pylint: disable=cell-var-from-loop
                    if not photo:
                        return '—'
                    return mark_safe(f'<img src="{photo.url}" width="100">')
                fn.short_description = 'Превью' # yapf: disable

                setattr(self, name, fn)
        super().__init__(*args, **kwargs)
