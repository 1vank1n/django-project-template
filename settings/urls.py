from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

# from django.contrib.sitemaps.views import sitemap

# from applications.core.sitemap import (SitemapWeekly, SitemapDaily)
# sitemaps = {'weekly': SitemapWeekly, 'daily': SitemapDaily}

# admin.site.site_header = 'Салехард.Онлайн'
# admin.site.site_title = 'Салехард.Онлайн'
# admin.site.index_title = ''

urlpatterns = [
    # path(
    #     'sitemap.xml/',
    #     sitemap,
    #     {'sitemaps': sitemaps},
    #     name='django.contrib.sitemaps.views.sitemap'
    # ),
    path(
        'admin/',
        admin.site.urls,
    ),
    # path(
    #     'ckeditor/',
    #     include('ckeditor_uploader.urls'),
    # ),
    path(
        '',
        include(('applications.main.urls', 'main'), namespace='main'),
    ),
]

urlpatterns += staticfiles_urlpatterns() + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
