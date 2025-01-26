import pytest


@pytest.fixture
def overridden_fixture():
    return "overridden_load_api_fixture_value"
