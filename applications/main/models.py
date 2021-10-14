from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from ..core.models import Common, PathAndRename, Seo, Single


class Page(
        Seo,
        Common,
):
    """
    Статические страницы
    """

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=200,
    )

    slug = models.SlugField(
        verbose_name='URL-имя',
        unique=True,
    )

    content = RichTextUploadingField(
        verbose_name='Контент',
    ) # yapf: disable

    class Meta:
        ordering = ['title']
        verbose_name = 'страница'
        verbose_name_plural = 'статические страницы'

    def get_absolute_url(self):
        return reverse('main:page_detail', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return self.title


class Preference(
        Single,
        models.Model,
):
    """
    Настройки
    """

    site_title = models.CharField(
        verbose_name='Название',
        max_length=100,
    )

    site_description = models.TextField(
        verbose_name='Описание',
        max_length=200,
        blank=True,
    )

    site_image = models.ImageField(
        verbose_name='Изображение сайта',
        upload_to=PathAndRename('main/preference/image'),
        help_text='JPG. 1200x800',
        blank=True,
    )

    site_phone = PhoneNumberField(
        verbose_name='Телефон',
    )  # yapf: disable

    site_email = models.CharField(
        verbose_name='Эл.почта',
        max_length=100,
    )

    #Подключать при наличии приложения capture
    # email_bids = models.TextField(
    #     verbose_name='Электронная почта для получения заявок на покупку',
    #     help_text='Каждая Электронная почта с новой строки',
    #     blank=True,
    # )

    # Подключать при наличии социальных сетей
    # social_facebook = models.CharField(
    #     verbose_name='Facebook',
    #     max_length=100,
    #     blank=True,
    # )

    # social_instagram = models.CharField(
    #     verbose_name='Instagram',
    #     max_length=100,
    #     blank=True,
    # )

    # social_telegram = models.CharField(
    #     verbose_name='Telegram',
    #     max_length=100,
    #     blank=True,
    # )

    # social_vkontakte = models.CharField(
    #     verbose_name='Vkontakte',
    #     max_length=100,
    #     blank=True,
    # )

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
