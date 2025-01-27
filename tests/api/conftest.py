import pytest


@pytest.fixture
def api_fixture():
    return "api_fixture_value"


@pytest.fixture
def overridden_fixture():
    return "original_api_fixture_value"
