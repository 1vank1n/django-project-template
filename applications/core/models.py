import os
import uuid

from django.db import models
from django.utils.deconstruct import deconstructible
from model_utils.managers import QueryManager


class Common(models.Model):
    """
    Абстрактный класс. Содержит `статус` и `время создания / модификации` объекта.
    """

    DRAFT = 'draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликовано'),
    )

    status = models.CharField(
        'Статус',
        choices=CHOICES_STATUS,
        default=PUBLISHED,
        max_length=50,
    )

    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        'Дата изменения',
        auto_now=True,
    )

    objects = models.Manager()
    published = QueryManager(status=PUBLISHED)

    class Meta:
        abstract = True
        ordering = ('-created',)


class MetaFields(models.Model):
    """
    Абстрактный класс. Содержит мета описание и ключевые слова.
    """

    meta_description = models.CharField(
        'META описание',
        max_length=200,
        help_text='Рекомендуемая длина мета описания = 160 символов.',
        blank=True,
        null=True,
    )

    meta_keywords = models.CharField(
        'META ключевые слова',
        max_length=2500,
        help_text='Укажите ключевые слова через запятую.',
        blank=True,
        null=True,
    )

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
