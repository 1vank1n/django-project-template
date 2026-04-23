from split_settings.tools import include, optional

include(
    'components/apps.py',
    'components/base.py',
    'components/axes.py',
    'components/logging.py',
    'components/security.py',
    'components/storages.py',
    'components/vite.py',
    'components/debug.py',
    optional('local_settings.py'),
)
