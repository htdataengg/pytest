import pytest

from pyt.functions import f2

# use finalizer to tear down - better
def teardown():
    print("\nteardown\n")


@pytest.fixture(autouse=True)
def setup(request):
    print("\nsetup")
    f2()
    request.addfinalizer(teardown)


def test_1():
    print("test_1\n")


def test_2():
    print("test_2\n")
