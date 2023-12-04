from django.db import models

from ..core.models import PathAndRename, Single


class Preference(Single):
    """
    Настройки
    """

    site_title = models.CharField(
        verbose_name='Название сайта',
        max_length=200,
        blank=True,
    )

    site_description = models.TextField(
        verbose_name='Описание сайта',
        blank=True,
    )

    site_photo = models.ImageField(
        verbose_name='Фотография сайта',
        upload_to=PathAndRename('main/preference/site_photo'),
        help_text='Загружать JPG с размерами 1200x630px',
        blank=True,
    )

    header_html = models.TextField(
        verbose_name='HEAD',
        help_text='Вставка html-кода для всех страниц сайта перед закрывающимся тегом HEAD',
        blank=True,
    )

    footer_html = models.TextField(
        verbose_name='FOOTER',
        help_text='Вставка html-кода для всех страниц сайта перед закрывающимся тегом FOOTER',
        blank=True,
    )

    class Meta:
        verbose_name = 'настройки'
        verbose_name_plural = 'настройки'

    def __str__(self):
        return 'Настройки'
