import pytest

from pyt.functions import f2


# use fixture for set up by using autouse=true

@pytest.fixture(autouse=True)
def setup():
    print("\nsetup")
    f2()


def test_1():
    print("test_1\n")


def test_2():
    print("test_2\n")
