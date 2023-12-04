from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

# admin.site.site_header = 'Example'
# admin.site.site_title = 'Example'
# admin.site.index_title = 'Example'

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
    ),
]

urlpatterns += [
    path(
        '',
        include(('applications.main.urls', 'main'), namespace='main'),
    ),
]

urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
