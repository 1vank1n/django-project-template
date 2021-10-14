from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from ..core.admin import CommonAdmin
from . import models


@admin.register(models.Page)
class PageAdmin(CommonAdmin):
    list_display = [
        'title',
        'status',
        'created',
        'modified',
    ]
    prepopulated_fields = {
        'slug': ['title'],
    }


@admin.register(models.Preference)
class PreferenceAdmin(SingleModelAdmin):
    pass


# подключать для изменения названия в административной панели
# admin.site.site_title = ''
# admin.site.site_header = ''
