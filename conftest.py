import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user(db):
    return get_user_model().objects.create_user(
        username='user',
        email='user@example.com',
        password='password',
    )


@pytest.fixture
def admin(db):
    return get_user_model().objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='password',
    )


@pytest.fixture
def auth_client(client, user):
    client.force_login(user)
    return client


@pytest.fixture
def admin_client(client, admin):
    client.force_login(admin)
    return client
