import nplusone
from django.conf import settings

# django-nplusone
if settings.DEBUG:
    nplusone.show_nplusones()

# django-querycount
# django-debug-toolbar
settings.MIDDLEWARE += [
    'querycount.middleware.QueryCountMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# django-debug-toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]
