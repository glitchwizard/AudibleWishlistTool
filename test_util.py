import util

def test_generate_key():
    result = util.generate_key()
    assert len(result) > 0


def test_get_key():
    result = util.get_key()
    assert len(result) > 0
