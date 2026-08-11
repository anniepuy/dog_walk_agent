import httpx

AIR_QUALITY_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

def get_air_quality(latitude: float, longitude: float) -> dict:
    """Return the current air quality for a latitude and longitude."""

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "us_aqi",
            "pm2_5",
            "pm10",
        ],
        "timezone": "auto",
    }

    response = httpx.get(
        AIR_QUALITY_URL,
        params=params,
        timeout=10.0,
    )

    response.raise_for_status()

    data = response.json()

    return {
        "current": data["current"],
        "units": data["current_units"],
    }