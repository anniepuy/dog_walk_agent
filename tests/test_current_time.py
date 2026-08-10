from tools.current_time import get_current_time

def test_get_current_time_returns_string():
    result = get_current_time()

    assert isinstance(result, str)
    assert len(result) >0