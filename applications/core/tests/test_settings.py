import os
import subprocess
import sys

import pytest


@pytest.mark.parametrize('debug_value, expected', [('off', False), ('on', True)])
def test_debug_mode_controls_development_integrations(debug_value, expected):
    subprocess.run(
        [
            sys.executable,
            '-c',
            f"""
import django
django.setup()
from django.conf import settings
from settings import BASE_DIR
from settings.components.base import BASE_DIR as component_base_dir
assert settings.DEBUG is {expected!r}
assert settings.BASE_DIR == component_base_dir == BASE_DIR
assert settings.DJANGO_VITE['default']['manifest_path'] == (
    BASE_DIR / 'static' / 'vite' / 'manifest.json'
)
assert ('debug_toolbar' in settings.INSTALLED_APPS) is {expected!r}
assert (
    'debug_toolbar.middleware.DebugToolbarMiddleware' in settings.MIDDLEWARE
) is {expected!r}
assert settings.DJANGO_VITE['default']['dev_mode'] is {expected!r}
""",
        ],
        env={
            **os.environ,
            'DJANGO_SETTINGS_MODULE': 'settings.settings',
            'DEBUG': debug_value,
            'SECRET_KEY': 'settings-test',
            'DATABASE_URL': 'sqlite:///:memory:',
        },
        check=True,
        capture_output=True,
        text=True,
    )
