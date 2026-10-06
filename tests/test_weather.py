from tools.weather import get_weather

# test NYC weather
def test_get_weather_returns_current_weather():
    result = get_weather(
        latitude=40.7128,
        longitude=74.0060,
    )

    assert isinstance(result, dict)
    assert "current" in result 
    assert "units" in result

    #python3.12 -c "from tools.weather import get_weather; print(get_weather(40.7128, -74.0060))"