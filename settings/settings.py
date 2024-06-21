from split_settings.tools import include, optional

include(
    'components/apps.py',
    'components/base.py',
    'components/debug.py',
    optional('local_settings.py'),
)
