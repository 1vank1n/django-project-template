from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from phonenumber_field.modelfields import PhoneNumberField

from ..main.models import Preference


class Bid(models.Model):
    """ Заявка """

    name = models.CharField(
        verbose_name='Название',
        max_length=100,
    )

    phone = PhoneNumberField(
        verbose_name='Телефон',
    )  # yapf: disable

    email = models.EmailField(
        verbose_name='Почта',
        max_length=100,
    )

    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-created']
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'

    def mail_admin(self):
        content = render_to_string(
            'capture/letters/mail_admin_bid.html',
            {
                'object': self,
                'domain': Site.objects.get_current().domain,
            },
        )
        preference = Preference.objects.first()
        if preference:
            email_list = preference.email_bids.split('\r\n')
            if email_list:
                msg = send_mail(
                    subject='Новая заявка. #{}'.format(self.pk),
                    message=content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=email_list,
                    html_message=content,
                )
                return msg
        return False

    def __str__(self):
        return f'{self.name} — {self.phone}'
