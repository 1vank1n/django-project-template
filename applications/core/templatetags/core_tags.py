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
