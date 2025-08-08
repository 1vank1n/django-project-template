import pytest

from applications.core.templatetags.core_tags import ru_plural


@pytest.mark.parametrize(
    'value, expected',
    [
        (1, 'подписчик'),
        (2, 'подписчика'),
        (5, 'подписчиков'),
        (21, 'подписчик'),
        (25, 'подписчиков'),
    ],
)
def test_ru_plural(value, expected):
    variants = 'подписчик,подписчика,подписчиков'
    assert ru_plural(value, variants) == expected
