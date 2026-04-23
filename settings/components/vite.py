from settings.components.base import BASE_DIR, DEBUG

DJANGO_VITE = {
    'default': {
        'dev_mode': DEBUG,
        'manifest_path': BASE_DIR / 'static' / 'vite' / 'manifest.json',
        'static_url_prefix': 'vite',
    },
}
