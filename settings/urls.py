from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^', include('apps.main.urls')),
]

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
