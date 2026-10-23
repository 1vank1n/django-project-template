from settings.components.base import DEBUG

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    'axes',
    'django_extensions',
    'django_vite',
    'extra_views',
    'health_check',
]

if DEBUG:
    THIRD_APPS += ['debug_toolbar']

CUSTOM_APPS = [
    'applications.core',
    'applications.main',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + CUSTOM_APPS + ['django_cleanup']
