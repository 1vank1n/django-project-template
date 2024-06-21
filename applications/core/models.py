import os
import uuid
from typing import Any

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.deconstruct import deconstructible
from model_utils.managers import QueryManager


class Date(models.Model):
    """
    Дата / абстрактный класс
    """

    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
    )

    class Meta:
        abstract = True
        ordering = ['-created']


class Common(Date):
    """
    Общий / абстрактный класс
    """

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Черновик'
        PUBLISHED = 'published', 'Опубликовано'

    status = models.CharField(
        verbose_name='Статус',
        choices=Status.choices,
        default=Status.PUBLISHED,
        max_length=50,
    )

    objects = models.Manager()
    drafted = QueryManager(status=Status.DRAFT)
    published = QueryManager(status=Status.PUBLISHED)

    class Meta(Date.Meta):
        abstract = True


class Seo(models.Model):
    """
    SEO / абстрактный класс
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
    )

    seo_keywords = models.CharField(
        verbose_name='SEO ключевые слова',
        max_length=2500,
        help_text='Укажите ключевые слова через запятую.',
        blank=True,
    )

    class Meta:
        abstract = True


class Single(models.Model):
    """
    Сингл / абстрактный класс
    Модель ограничивает класс одним инстансом
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs) -> None:
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError('Может быть только один объект этого класса')
        return super().save(*args, **kwargs)


class Metadata(models.Model):
    """Метадата / абстрактный клас"""

    metadata = models.JSONField(
        default=dict,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True

    def get_value_from_metadata(self, key: str, default: Any = None) -> Any:
        return self.metadata.get(key, default)

    def store_value_in_metadata(self, items: dict) -> None:
        if not self.metadata:
            self.metadata = {}
        self.metadata.update(items)
        return None

    def clear_metadata(self) -> None:
        self.metadata = {}
        return None

    def delete_value_from_metadata(self, key: str) -> None:
        if key in self.metadata:
            del self.metadata[key]
            return None


@deconstructible
class PathAndRename:
    """
    Класс используется для генерации уникальных имён в FileField, ImageField
    Ex.: upload_to=PathAndRename('app/model/field')
    """

    def __init__(self, sub_path: str) -> None:
        self.path = sub_path

    def __call__(self, _, filename: str) -> str:
        _, extension = os.path.splitext(filename)
        filename = f'{uuid.uuid4().hex}{extension}'
        return os.path.join(self.path, filename)
