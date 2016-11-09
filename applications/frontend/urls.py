from django.conf.urls import url
from .views import FrontendView


urlpatterns = [
    url(r'^(?P<slug>.*)$', FrontendView.as_view(), name='template'),
]
