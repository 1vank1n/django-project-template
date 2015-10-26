from django.conf.urls import patterns, include, url
from .views import FrontendView


urlpatterns = patterns('apps.frontend.views',
    url(r'^(?P<slug>.*)$', FrontendView.as_view(), name='template'),
)
