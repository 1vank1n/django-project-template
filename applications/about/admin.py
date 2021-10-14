from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from . import models


@admin.register(models.About)
class AboutAdmin(SingleModelAdmin):
    pass


#подключать при наличии models.Location
# @admin.register(models.Location)
# class LocationAdmin(SingleModelAdmin):
#     pass
