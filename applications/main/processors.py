from . import models


def preference(*args, **kwargs):
    return {
        'preference': models.Preference.objects.first() or {},
    }
