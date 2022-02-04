from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from . import models


@admin.register(models.Preference)
class PreferenceAdmin(SingleModelAdmin):
    pass
