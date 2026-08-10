import httpx

WEATHER_URL = "https://api.open-mateo.com/v1/forecast"

def get_weather(latitude: float, longitude: float)-> dict:
    """Return the current weather for a latitude and longitude."""

    params = {
        
    }