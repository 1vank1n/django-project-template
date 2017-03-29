# -*- coding: utf-8 -*-
# from django.contrib.sitemaps import Sitemap
# from itertools import chain
# from django.core.urlresolvers import reverse

# from applications.main.models import News


# class SitemapWeekly(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.8

#     def items(self):
#         return list(
#             chain(
#                 News.published.all(),
#                 ...
#             )
#         )

#     def lastmod(self, obj):
#         return obj.created


# class SitemapDaily(Sitemap):
#     changefreq = 'weekly'
#     priority = 1

#     def items(self):
#         return [
#             'main:index',
#             ...
#         ]

#     def location(self, item):
#         return reverse(item)
