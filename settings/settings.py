from split_settings.tools import optional, include

include(
    'components/apps.py',
    'components/base.py',
    'components/debug.py',
    optional('local_settings.py'),
)
