# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
# from django.contrib.sitemaps.views import sitemap

# from applications.main.sitemap import (SitemapWeekly, SitemapDaily)
# sitemaps = {'weekly': SitemapWeekly, 'daily': SitemapDaily}


urlpatterns = [
    # url(r'^sitemap\.xml$',
    #     sitemap,
    #     {'sitemaps': sitemaps}),

    url(r'^admin/',
        include(admin.site.urls)),

    # url(r'^ckeditor/',
    #     include('ckeditor_uploader.urls')),

    url(r'^',
        include('applications.main.urls', namespace='main')),
]

urlpatterns += staticfiles_urlpatterns() + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
