from tools.location import get_coordinates

def test_get_coordinates_returns_location_data():
    result = get_coordinates("Atlanta, Georgia")

    assert isinstance(result, dict)
    assert "latitude" in result
    assert "longitude" in result
    assert "timezone"  in result
    