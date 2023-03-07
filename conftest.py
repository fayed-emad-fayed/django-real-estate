import pytest
from pytest_factoryboy import register

from tests.factories import ProfileFactory, UserFactory


register(ProfileFactory)
register(UserFactory)

@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user

@pytest.fixture
def create_superuser(db, user_factory):
    super_user = user_factory.create(is_staff=True, is_superuser=True)
    return super_user

@pytest.fixture
def profile(db, profile_factory):
    profile = profile_factory.create()
    return profile