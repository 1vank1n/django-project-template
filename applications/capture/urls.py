from django.urls import path

from . import views

urlpatterns = [
    path(
        'bid/create/',
        views.AjaxBidCreateView.as_view(),
        name='bid_create',
    ),
]
