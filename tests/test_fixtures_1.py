import pytest

from pyt.functions import f2

# use fixture for set up by calling it in each method
@pytest.fixture()
def setup():
    print("\nsetup")
    f2()


def test_1(setup):
    print("test_1\n")


def test_2(setup):
    print("test_2\n")
