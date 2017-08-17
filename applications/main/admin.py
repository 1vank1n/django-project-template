from django.contrib import admin
from . import models


class CommonAdmin(admin.ModelAdmin):
    list_filter = ('status', 'created', )
    readonly_fields = ('created', 'modified', )
    actions = ['make_published', 'make_drafted', ]

    def make_published(modeladmin, request, queryset):
        queryset.update(status=models.Common.PUBLISHED)
    make_published.short_description = u'Выставить статус "Опубликовано"'

    def make_drafted(modeladmin, request, queryset):
        queryset.update(status=models.Common.DRAFT)
    make_drafted.short_description = u'Выставить статус "Черновик"'


class MetaFieldsAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        newfieldsets = list(fieldsets)
        fields = ['meta_keywords', 'meta_description']
        for f in fields:
            newfieldsets[0][1]['fields'].remove(f)
        newfieldsets.append(
            [u'Мета-информация', {'classes': ('collapse',), 'fields': fields}])
        return newfieldsets
