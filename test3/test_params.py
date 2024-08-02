import pytest


@pytest.fixture(params=[1, 2, 3])
def setup(request):
    return request.param


def test_1(setup):
    print(f"setup: {setup}")
    assert True
