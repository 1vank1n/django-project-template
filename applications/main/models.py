# -*- coding: utf-8 -*-
import os
import uuid
from django.db import models
# from django.core.urlresolvers import reverse
from django.utils.deconstruct import deconstructible
# from django.utils.safestring import mark_safe
# from django.utils.timezone import now

# from ckeditor_uploader.fields import RichTextUploadingField
from model_utils.managers import QueryManager


"""
    Общее
"""


class Common(models.Model):

    DRAFT = 'draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
        (DRAFT, u'Черновик'),
        (PUBLISHED, u'Опубликовано'),
    )

    status = models.CharField(
        u'Статус',
        choices=CHOICES_STATUS,
        default=PUBLISHED,
        max_length=50)

    created = models.DateTimeField(
        u'Дата создания',
        auto_now_add=True)

    modified = models.DateTimeField(
        u'Дата изменения',
        auto_now=True)

    objects = models.Manager()
    published = QueryManager(status=PUBLISHED)

    class Meta:
        abstract = True
        ordering = ('-created', )


class MetaFields(models.Model):

    meta_description = models.CharField(
        u'META описание',
        max_length=200,
        help_text=u'Рекомендуемая длина мета описания = 160 символов.',
        blank=True,
        null=True)

    meta_keywords = models.CharField(
        u'META ключевые слова',
        max_length=2500,
        help_text=u'Укажите ключевые слова через запятую.',
        blank=True,
        null=True)

    class Meta:
        abstract = True


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        basename, extension = os.path.splitext(filename)
        filename = '{}{}'.format(uuid.uuid4().hex, extension)
        return os.path.join(self.path, filename)
