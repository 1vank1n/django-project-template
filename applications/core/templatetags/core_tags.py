import json

from django import template

from applications.core.models import Common

register = template.Library()


@register.filter
def published(value):
    return value.filter(status=Common.STATUS.published)


@register.filter
def to_json(value):
    return json.dumps(value)


@register.filter
def ru_plural(value, variants):
    """
    Множественные окончания для русских слов.

    Пример:
        1 подписчик
        3 подписчика
        20 подписчиков

        {{ total_followers|ru_plural:'подписчик,подписчика,подписчиков' }}
    """

    variants = variants.split(',')
    value = abs(int(value))

    if value % 10 == 1 and value % 100 != 11:
        variant = 0
    elif value % 10 >= 2 and value % 10 <= 4 and (value % 100 < 10 or value % 100 >= 20):
        variant = 1
    else:
        variant = 2

    return variants[variant]
