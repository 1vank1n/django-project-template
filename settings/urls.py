from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from health_check.views import HealthCheckView


class ProjectHealthCheckView(HealthCheckView):
    checks = (
        'health_check.checks.Cache',
        'health_check.checks.Database',
        'health_check.checks.Storage',
    )


# admin.site.site_header = 'Django Project Template'
# admin.site.site_title = 'Django Project Template'
# admin.site.index_title = 'Django Project Template'

urlpatterns = [
    path(
        'admin/doc/',
        include('django.contrib.admindocs.urls'),
    ),
    path(
        'admin/',
        admin.site.urls,
    ),
    path(
        'health/',
        ProjectHealthCheckView.as_view(),
        name='health_check',
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
