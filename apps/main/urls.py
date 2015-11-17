from django.conf.urls import url
from .views import IndexView
# from .sitemap import SitemapWeekly, SitemapDaily

# sitemaps = {'weekly':SitemapWeekly, 'daily':SitemapDaily}

# urlpatterns = patterns ('',
#     # sitemap
#     url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
# )

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^exmple-slug/(?P<slug>[-\w]+)/$', 'example_list', {'template': 'example_list.html'}, name='main.example.list'),
    # url(r'^example-id/(?P<id>\d+)/$', 'example_list', {'template': 'example_list.html'}, name='main.example.list'),
]
