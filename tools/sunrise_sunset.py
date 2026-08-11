import httpx

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

def get_sunrise_sunset(
        latitude: float,
        longitude: float, 
        timezone: str,
) -> dict:
    """Return today's sunrise and sunset for a location."""

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": [
            "sunrise",
            "sunset",
        ],
        "timezone": timezone,
        "forecast_days": 1,
    }

    response = httpx.get(
        FORECAST_URL,
        params=params,
        timeout=10.0,
    )

    response.raise_for_status()

    data = response.json()

    return {
        "date": data["daily"]["time"][0],
        "sunrise": data["daily"]["sunrise"][0],
        "sunset": data["daily"]["sunset"][0],
        "timezone": data["timezone"],
    }