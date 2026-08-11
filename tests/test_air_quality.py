from tools.air_quality import get_air_quality

def test_get_air_quality_returns_current_data():
    result = get_air_quality(
        latitude=33.749,
        longitude=84.38798,
    )

    assert isinstance(result, dict)
    assert "current" in result
    assert "units" in result
    assert "us_aqi" in result["current"]
