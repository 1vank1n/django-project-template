from django.urls import path

from . import views

urlpatterns = [
    path(
        'bid/create/',
        views.BidAjaxCreateView.as_view(),
        name='bid_ajax_create',
    ),
]
