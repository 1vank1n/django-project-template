from django.contrib import admin

from . import models


@admin.register(models.Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'phone',
        'email',
        'created',
    ]
    search_fields = [
        'name',
        'phone',
    ]
    date_hierarchy = 'created'
