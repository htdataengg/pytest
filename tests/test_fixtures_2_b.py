import pytest

from pyt.functions import f2

# use yield to tear down

@pytest.fixture(autouse=True)
def setup(request):
    print("\nsetup")
    f2()
    yield
    print("\nteardown\n")


def test_1():
    print("test_1\n")


def test_2():
    print("test_2\n")
