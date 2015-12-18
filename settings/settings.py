import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "{{ secret_key }}"

DEBUG = False
ALLOWED_HOSTS = []
ADMINS = (
    ('Ivan Lukyanets', 'ivan@il-studio.ru'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    ## 3rd packages
    # 'adminsortable',
    # 'treebeard',
    # 'ckeditor',
    # 'sorl.thumbnail',
    # 'django_settings',

    # apps
    'apps.main',
    'apps.frontend',

    # 'django_cleanup',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'apps.main.processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'mysql_client',
        'PASSWORD': 'mysql_password'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static_nginx')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# django-smtp-ssl
# https://github.com/bancek/django-smtp-ssl

# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = ''
# EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'


# CKEDITOR
# https://github.com/django-ckeditor/django-ckeditor

# CKEDITOR_UPLOAD_PATH = 'uploads/'
# CKEDITOR_IMAGE_BACKEND = 'pillow'
# CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': [["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
#                 ['Blockquote'],
#                 ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
#                  'JustifyRight', 'JustifyBlock'],
#                 ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"], ['Undo', 'Redo'], ["Source"],
#                 ["Maximize"]],
#         'width': 900
#     },
# }


try:
    from local_settings import *
except ImportError:
    pass
