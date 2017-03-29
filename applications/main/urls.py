# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.IndexView.as_view(),
        name='index'),

    # url(r'^exmple-slug/(?P<slug>[-\w]+)/$',
    #     views.IndexView.as_view(),
    #     name='example_detail'),

    # url(r'^example-id/(?P<id>\d+)/$',
    #     views.IndexView.as_view(),
    #     name='example_detail'),
]
