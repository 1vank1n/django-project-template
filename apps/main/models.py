# coding: utf-8
# import os, uuid
from django.db import models
# from treebeard.mp_tree import MP_Node
# from django.utils.timezone import now
from django.core.urlresolvers import reverse
from django.utils.deconstruct import deconstructible

# https://github.com/iambrandontaylor/django-admin-sortable
# from adminsortable.models import Sortable, SortableForeignKey

# https://github.com/django-ckeditor/django-ckeditor
# from ckeditor.fields import RichTextField

# https://github.com/jperelli/django-settings
# import django_settings


# @deconstructible
# class PathAndRename(object):
#     def __init__(self, sub_path):
#         self.path = sub_path

#     def __call__(self, instance, filename):
#         basename, extension = os.path.splitext(filename)
#         filename = '{}{}'.format(uuid.uuid4().hex, extension)
#         return os.path.join(self.path, filename)


## Treebeard Example
# class Service(MP_Node):
#     title = models.CharField(u'Название', max_length=150)
#     photo = models.ImageField(u'Фото', upload_to=PathAndRename('service'), help_text=u'160x160', null=True, blank=True)
#     created = models.DateTimeField(u'Дата создания', default=now)
#     status = models.BooleanField(u'Статус', default=True)
#     meta_description = models.CharField(max_length=200, blank=True)
#     meta_keywords = models.CharField(max_length=50, blank=True)

#     class Meta:
#         # ordering = ('order',)
#         verbose_name = u'услугу'
#         verbose_name_plural = u'Услуги'

#     def get_absolute_url(self):
#         return reverse('main.service', kwargs={'slug':self.slug})

#     def __unicode__(self):
#         return self.title


# class ServicePhoto(Sortable):
#     class Meta(Sortable.Meta):
#         pass

#     service = SortableForeignKey(Service)
#     photo = models.ImageField(u'Фото', upload_to=PathAndRename('service'))


#     def __unicode__(self):
#         return ''


## Sortable Model
# class Example(Sortable):
#     title = models.CharField(u'Название', max_length=150)
#     photo = models.ImageField(u'Фото', upload_to=PathAndRename('example'), help_text=u'widthXheight')
#     created = models.DateTimeField(u'Дата создания', default=now)
#     status = models.BooleanField(u'Статус', default=True)

#     class Meta:
#         ordering = ('order',)
#         verbose_name = u'example'
#         verbose_name_plural = u'examples'

#     def get_absolute_url(self):
#         return reverse('main.example', kwargs={'id':self.id})

#     def __unicode__(self):
#         return self.title


# DJANGO_SETTINGS

# class Text(django_settings.db.Model):
#     value = models.TextField()
#     class Meta:
#         abstract = True   # it's IMPORTANT - it need to be abstract
# django_settings.register(Text)


# class Image(django_settings.db.Model):
#     value = models.ImageField(
#         u'Фото',
#         upload_to=PathAndRename('settings')
#     )
#     class Meta:
#         abstract = True   # it's IMPORTANT - it need to be abstract
# django_settings.register(Image)


# class Docs(django_settings.db.Model):
#     value = models.FileField(
#         u'Документ',
#         upload_to=PathAndRename('settings')
#     )
#     class Meta:
#         abstract = True   # it's IMPORTANT - it need to be abstract
# django_settings.register(Docs)


# class HTMLText(django_settings.db.Model):
#     value = RichTextField(u'Текст')
#     class Meta:
#         abstract = True   # it's IMPORTANT - it need to be abstract
# django_settings.register(HTMLText)

