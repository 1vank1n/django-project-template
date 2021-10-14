from django.views import generic

from . import models
from ..core.mixins import StaffQuerysetMixin


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class PageDetailView(
        StaffQuerysetMixin,
        generic.DetailView,
):
    template_name = 'main/page_detail.html'
    model = models.Page
    queryset = model.published.all()
