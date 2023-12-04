DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

THIRD_APPS = [
    'debug_toolbar',
    'django_extensions',
    'extra_views',
    'spurl',
]

CUSTOM_APPS = [
    'applications.core',
    'applications.main',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + CUSTOM_APPS + ['django_cleanup']
