from _pytest.python_api import raises

from pyt.failing_code import badcode


def test_bad_code():
    with raises(ValueError):
        badcode()