def test_functional_api(common_fixture, api_fixture, overridden_fixture):
    assert common_fixture == "common_fixture_value"
    assert api_fixture == "api_fixture_value"
    assert overridden_fixture == "original_api_fixture_value"
