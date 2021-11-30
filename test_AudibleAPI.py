import AudibleAPI

def test_get_wishlist():
    result = AudibleAPI.get_wishlist()
    assert len(result) > 0
    assert isinstance(result, list)
    if len(result) > 0:
        assert 'asin' in result[0]