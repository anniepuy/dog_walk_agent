import httpx

WEATHER_URL = "https://api.open-mateo.com/v1/forecast"

def get_weather(latitude: float, longitude: float)-> dict:
    """Return the current weather for a latitude and longitude."""

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "apparent_temperature",
            "relative_humidity_2m",
            "precipitation",
            "weather_code",
            "wind_speed_10m",
        ],
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "timezone": "auto"
    }

    response = httpx.get(
        WEATHER_URL,
        params=params,
        timeout=10.0
    )

    response.raise_for_status()

    data=response.json()

    return{
        "current": data["current"],
        "units": data["current_units"],
    }