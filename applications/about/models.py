from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from ..core.models import PathAndRename, Single


class About(Single):
    """ О cайте """

    title = models.CharField(
        verbose_name='Название',
        max_length=100,
    )

    content = RichTextUploadingField(
        verbose_name='Контент',
    )  # yapf: disable

    image = models.ImageField(
        verbose_name='Изображение',
        upload_to=PathAndRename('main/about/image'),
        blank=True,
    )

    class Meta:
        verbose_name = 'о сайте'
        verbose_name_plural = 'о сайте'

    def __str__(self):
        return self.title


# подключать при наличии расположения
# class Location(Single):
#     """ Расположение """

#     title = models.CharField(
#         verbose_name='Название',
#         max_length=100,
#     )

#     content = RichTextUploadingField(
#         verbose_name='Контент',
#     )  # yapf: disable

#     image = models.ImageField(
#         verbose_name='Изображение',
#         upload_to=PathAndRename('main/location/image'),
#         blank=True,
#     )

#     class Meta:
#         verbose_name = 'расположение'
#         verbose_name_plural = 'расположение'

#     def __str__(self):
#         return self.title
