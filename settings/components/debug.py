from django.conf import settings

if settings.DEBUG:
    settings.MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

INTERNAL_IPS = [
    '127.0.0.1',
]
