def test_ui(common_fixture, ui_fixture):
    assert common_fixture == "common_fixture_value"
    assert ui_fixture == "ui_fixture_value"
