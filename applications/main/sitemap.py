# coding: utf-8
import datetime
from django.contrib.sitemaps import Sitemap
from django.db.models import Q
from itertools import chain
from django.core.urlresolvers import reverse
# from .models import Example

# class SitemapWeekly(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.8

#     def items(self):
#         service_list = Service.objects.filter(status=True)
#         news_list = News.objects.filter(status=True)
#         return list(chain(service_list, news_list))

#     def lastmod(self, obj):
#         return obj.created

# class SitemapDaily(Sitemap):
#     changefreq = 'daily'
#     priority = 1

#     def items(self):
#         return ['main.index', 'main.service.all', 'main.personal.list', 'main.offer.list', 'main.review', 'main.contacts',]

#     def location(self, item):
#         return reverse(item)
