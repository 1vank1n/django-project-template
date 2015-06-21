from django.conf.urls import patterns, include, url
# from .sitemap import SitemapWeekly, SitemapDaily

# sitemaps = {'weekly':SitemapWeekly, 'daily':SitemapDaily}

# urlpatterns = patterns ('',
#     # sitemap
#     url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
# )

urlpatterns += patterns('apps.main.views',
    url(r'^$', 'index', {'template': 'index.html'}, name='main.index'),
    # url(r'^exmple-slug/(?P<slug>[-\w]+)/$', 'example_list', {'template': 'example_list.html'}, name='main.example.list'),
    # url(r'^example-id/(?P<id>\d+)/$', 'example_list', {'template': 'example_list.html'}, name='main.example.list'),
)
