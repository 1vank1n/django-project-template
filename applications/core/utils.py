from django.conf import settings
from django.contrib.admin.models import ADDITION, LogEntry
from django.contrib.admin.options import get_content_type_for_model
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.template.loader import render_to_string

from ..main.models import Preference


def logger(
    *,
    obj,
    user,
    message,
    action_flag=ADDITION,
):
    """Записать в LogEntry сообщение по объекту"""
    LogEntry.objects.log_action(
        user_id=user.pk,
        content_type_id=get_content_type_for_model(obj).pk,
        object_id=obj.pk,
        object_repr=str(obj),
        action_flag=action_flag,
        change_message=message,
    )


def mail(
    *,
    template_name,
    context_dict,
    email_list,
    subject,
):
    """Шаблонизация и отправка письма"""
    context = {
        'domain': Site.objects.get_current().domain,
        'preference': Preference.objects.first() or {},
    }
    context.update(context_dict)
    content = render_to_string(template_name, context)
    msg = send_mail(
        subject=subject,
        message=content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=email_list,
        html_message=content,
    )
    return msg
