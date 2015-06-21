# coding: utf-8
from django.contrib import admin
# from treebeard.admin import TreeAdmin
# from treebeard.forms import movenodeform_factory
# from adminsortable.admin import SortableAdmin, SortableStackedInline, NonSortableParentAdmin
# from .models import Example


# class ServicePhotoInline(SortableStackedInline):
#     model = ServicePhoto
#     extra = 1


# class ServiceAdmin(NonSortableParentAdmin, TreeAdmin):
#     form = movenodeform_factory(Service)
#     list_display = ('title', 'price', 'created', 'status',)
#     prepopulated_fields = {'slug': ('title',)}
#     search_fields = ('title',)
#     inlines = [ServicePhotoInline]
# admin.site.register(Service, ServiceAdmin)


# class NewsAdmin(SortableAdmin):
#     list_display = ('title', 'get_absolute_url', 'created', 'status',)
#     prepopulated_fields = {'slug': ('title',)}
# admin.site.register(News, NewsAdmin)
