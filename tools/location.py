import httpx

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

def get_coordinates(location: str) -> dict:
    """Return latitude and longitude for a city or location name."""
    params = {
        "name": location,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    response = httpx.get(
        GEOCODING_URL,
        params=params,
        timeout=10.0,
    )

    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        return {
            "error": f"Location not found: {location}"
        }

    result = data["results"][0]

    return {
        "name": result["name"],
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "country": result.get("country"),
        "timezone": result.get("timezone"),
    }