from tools.sunrise_sunset import get_sunrise_sunset

def test_get_sunrise_sunset_returns_daily_times():
    result = get_sunrise_sunset(
        latitude=33.749,
        longitude=84.38798,
        timezone="America/New_York",
    )

    assert isinstance(result, dict)
    assert "sunrise" in result
    assert "sunset" in result
    assert "timezone" in result
