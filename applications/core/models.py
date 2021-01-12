import os
import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.deconstruct import deconstructible
from model_utils import Choices
from model_utils.managers import QueryManager


class Common(models.Model):
    """
    Абстрактный класс. Содержит `статус` и `время создания / модификации` объекта.
    """

    STATUS = Choices(
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )

    status = models.CharField(
        verbose_name='Статус',
        choices=STATUS,
        default=STATUS.published,
        max_length=50,
    )

    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
    )

    objects = models.Manager()
    published = QueryManager(status=STATUS.published)

    class Meta:
        abstract = True
        ordering = ['-created']


class SeoFields(models.Model):
    """
    Абстрактный класс. Содержит мета описание и ключевые слова.
    """

    seo_title = models.CharField(
        verbose_name='SEO заголовок',
        max_length=100,
        help_text='Если заполнено, то используется вместо заголовка в title',
        blank=True,
    )

    seo_description = models.CharField(
        verbose_name='SEO описание',
        max_length=200,
        help_text='Рекомендуемая длина мета описания = 160 символов.',
        blank=True,
        null=True,
    )

    seo_keywords = models.CharField(
        verbose_name='SEO ключевые слова',
        max_length=2500,
        help_text='Укажите ключевые слова через запятую.',
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class Single(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError('Может быть только один объект этого класса')
        return super().save(*args, **kwargs)


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        _, extension = os.path.splitext(filename)
        filename = '{}{}'.format(uuid.uuid4().hex, extension)
        return os.path.join(self.path, filename)
