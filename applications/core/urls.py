from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.IndexView.as_view(),
        name='index',
    ),

    # path(
    #     'exmple-slug/<slug>/$',
    #     views.IndexView.as_view(),
    #     name='example_detail'
    # ),

    # path(
    #     'example-id/<pk>/$',
    #     views.IndexView.as_view(),
    #     name='example_detail'
    # ),
]
