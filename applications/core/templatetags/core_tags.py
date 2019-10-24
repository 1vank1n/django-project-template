import json
import re

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
def get_youtube_id(value):
    pattern = r'(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})'
    g = re.search(pattern, value)
    if g:
        return g.groups()[0]
    return value
