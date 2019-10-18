import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# CKEDITOR
# https://github.com/django-ckeditor/django-ckeditor

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Format', 'Bold', 'Italic', 'Underline', 'Strike',  'SpellChecker'],
            ['Blockquote', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', 'Indent', 'Outdent', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Image', 'Table', 'Link', 'Unlink', 'Anchor', 'SectionLink', 'Subscript', 'Superscript'],
            ['Undo', 'Redo'],
            ['Embed', 'Iframe'],
            ['Source'],
            ['Maximize']
        ],
        'width': 980,
        'extraPlugins': ','.join(
        [
            'embed',
            'iframe',
        ]),
    },
}
